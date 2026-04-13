import os
import json
import logging
from google import genai
from google.genai import types
from dotenv import load_dotenv
from prompts import (
    SYSTEM_PROMPT,
    INPUT_ENHANCEMENT_PROMPT,
    RAG_CONTEXT_PROMPT,
    SCENE_GENERATION_PROMPT,
    FORMAT_VALIDATION_PROMPT,
    AUTO_FIX_PROMPT,
    ITERATION_INTENSE_PROMPT,
    ITERATION_HUMOROUS_PROMPT,
    ITERATION_DIALOGUE_ONLY_PROMPT
)
from rag_manager import RAGManager

load_dotenv()

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    filename='pipeline.log',
    filemode='a'
)
logger = logging.getLogger("ScriptPipeline")

class ScriptPipeline:
    def __init__(self, api_key=None):
        self.api_key = api_key or os.getenv("GOOGLE_API_KEY")
        if self.api_key:
            self.client = genai.Client(api_key=self.api_key)
        else:
            self.client = None
            logger.error("No GOOGLE_API_KEY found.")
        
        self.rag_manager = RAGManager()
        self.history = [] # Memory context

    def _call_llm(self, messages, response_format=None):
        """
        Generic LLM call helper for the new google-genai SDK with rotation and high persistence.
        """
        if not self.client:
            return "ERROR: No API key provided."

        import time
        import random
        max_retries = 10 # Increased retries
        retry_delay = 5  # Higher initial delay for free tier
        
        # Models that are verified as available in this environment
        model_pool = [
            "gemini-2.5-flash",
            "gemini-2.0-flash",
            "gemini-flash-latest",
            "gemini-3-flash-preview"
        ]

        for attempt in range(max_retries):
            # Rotate model each attempt if hitting quota
            model_name = model_pool[attempt % len(model_pool)]
            
            try:
                # Convert OpenAI-style messages to Gemini components
                system_instruction = ""
                user_prompt = ""
                
                for msg in messages:
                    if msg["role"] == "system":
                        system_instruction += msg["content"] + "\n"
                    elif msg["role"] == "user":
                        user_prompt += msg["content"] + "\n"

                # Log the prompt for versioning/tracking
                logger.info(f"Calling LLM ({model_name}, Attempt {attempt+1})")

                config = {
                    "temperature": 0.9,
                    "system_instruction": system_instruction if system_instruction else None,
                }
                
                if response_format and response_format.get("type") == "json_object":
                    config["response_mime_type"] = "application/json"

                response = self.client.models.generate_content(
                    model=model_name,
                    contents=user_prompt,
                    config=types.GenerateContentConfig(**config)
                )
                
                # Check for safety filter blocks
                if response.candidates and response.candidates[0].finish_reason == "SAFETY":
                    logger.error("Response blocked by safety filters.")
                    return "ERROR: The AI model blocked this response due to safety filters. Please try a different scenario."

                if not response.text:
                    logger.warning(f"Empty response from LLM on attempt {attempt+1}.")
                    if attempt < max_retries - 1:
                        time.sleep(retry_delay)
                        continue
                    return "ERROR: The AI returned an empty response after multiple attempts."
                    
                text = response.text
                
                # Robust extraction of content from markdown blocks
                import re
                
                # Try to find content within ```json ... ``` or just ``` ... ```
                json_match = re.search(r'```json\s*(.*?)\s*```', text, re.DOTALL)
                if json_match:
                    text = json_match.group(1).strip()
                else:
                    generic_match = re.search(r'```\s*(.*?)\s*```', text, re.DOTALL)
                    if generic_match:
                        text = generic_match.group(1).strip()
                    else:
                        # No backticks? Clean common intro/outro lines
                        lines = text.splitlines()
                        if lines and (lines[0].lower().startswith("here") or ":" in lines[0]):
                             if len(lines[0]) < 50:
                                 text = "\n".join(lines[1:]).strip()
                
                logger.info(f"LLM call successful. Text length: {len(text)}")
                return text
                    
            except Exception as e:
                error_msg = str(e)
                print(f"DEBUG: Gemini Error: {error_msg}") # Print to terminal for visibility
                # Handle both rate limits and temporary service unavailability
                if any(err in error_msg for err in ["429", "RESOURCE_EXHAUSTED", "503", "UNAVAILABLE", "high demand"]):
                    wait_time = retry_delay + random.uniform(2, 5)
                    logger.warning(f"Temporary API issue ({error_msg[:30]}...). Retrying in {wait_time:.1f}s... (Attempt {attempt+1}/{max_retries})")
                    time.sleep(wait_time)
                    retry_delay *= 1.5 # Stronger backoff
                    continue
                
                logger.error(f"Error calling Gemini: {error_msg}")
                import traceback
                logger.error(traceback.format_exc()) # Log full traceback
                return f"ERROR: API Call failed - {error_msg[:100]}"
        
        logger.error("Max retries exceeded for LLM call.")
        return "ERROR: The AI system is currently overloaded. Please wait 30 seconds and try again."

    def transform_user_input(self, raw_input):
        """
        Transforms raw user input into an enriched structured format using LLM.
        """
        messages = [
            {"role": "system", "content": "You are a professional script consultant."},
            {"role": "user", "content": INPUT_ENHANCEMENT_PROMPT.format(raw_input=raw_input)}
        ]
        
        enriched_json = self._call_llm(messages, response_format={"type": "json_object"})
        
        if not enriched_json or enriched_json.startswith("ERROR:"):
            return self._get_fallback_input(raw_input)
            
        try:
            data = json.loads(enriched_json)
            # Basic validation of expected fields
            required_fields = ["genre", "style", "language", "length", "characters", "setting", "time", "tone", "goal"]
            for field in required_fields:
                if field not in data:
                    if field == "language":
                        data["language"] = "English"
                    elif field == "length":
                        data["length"] = "Medium (3-5 pages)"
                    else:
                        raise ValueError(f"Missing required field: {field}")
            
            # Add to history
            self.history.append({"input": raw_input, "structured": data})
            return data
        except Exception as e:
            logger.warning(f"Enrichment parsing failed: {str(e)}. Attempting regex recovery.")
            import re
            json_match = re.search(r'\{.*\}', enriched_json, re.DOTALL)
            if json_match:
                try:
                    data = json.loads(json_match.group())
                    if "language" not in data: data["language"] = "English"
                    if "length" not in data: data["length"] = "Medium (3-5 pages)"
                    self.history.append({"input": raw_input, "structured": data})
                    return data
                except:
                    pass
            return self._get_fallback_input(raw_input)

    def _get_fallback_input(self, raw_input):
        return {
            "genre": "Drama",
            "style": "Hollywood",
            "language": "English",
            "length": "Medium (3-5 pages)",
            "characters": [
                {"name": "ELIAS VANCE", "role": "Protagonist", "traits": "World-weary, cynical, former detective"},
                {"name": "SARAH CHASE", "role": "Antagonist", "traits": "Calculating, cold, corporate executive"}
            ],
            "setting": "A dimly lit, smoke-filled office in a forgotten corner of the city",
            "time": "LATE NIGHT",
            "tone": "Noir-inspired, tense, and heavy with regret",
            "goal": raw_input
        }

    def generate_scene(self, structured_input):
        """
        Main generation pipeline.
        """
        # 1. Retrieve context
        query = f"{structured_input['genre']} {structured_input['tone']} {structured_input['goal']}"
        retrieved = self.rag_manager.retrieve(query)
        context_text = "\n\n".join(retrieved) if retrieved else "No relevant examples found."
        
        # 2. Build full prompt
        language = structured_input.get('language', 'English')
        system_content = SYSTEM_PROMPT.format(language=language)
        
        # Format characters
        char_desc = "\n".join([f"* {c['name']} ({c['role']}): {c['traits']}" for c in structured_input['characters']])
        
        # Scene Prompt
        scene_prompt = SCENE_GENERATION_PROMPT.format(
            style=structured_input.get('style', 'Hollywood'),
            genre=structured_input['genre'],
            language=language,
            length=structured_input.get('length', 'Medium (3-5 pages)'),
            setting=structured_input['setting'],
            time=structured_input['time'],
            tone=structured_input['tone'],
            character_descriptions=char_desc,
            goal=structured_input['goal']
        )
        
        # Context Prompt
        context_prompt = RAG_CONTEXT_PROMPT.format(
            retrieved_examples=context_text,
            language=language
        )
        
        messages = [
            {"role": "system", "content": system_content},
            {"role": "user", "content": f"{context_prompt}\n\n{scene_prompt}"}
        ]
        
        # 3. Generate initial scene
        generated_scene = self._call_llm(messages)
        
        if generated_scene.startswith("ERROR:"):
            return generated_scene

        # 4. Evaluate & Auto-fix loop (Optimized: Only run if scene is suspiciously short)
        if len(generated_scene) < 500:
            logger.info("Scene too short. Triggering evaluation/fix layer.")
            final_scene = self.evaluate_and_fix(generated_scene)
        else:
            final_scene = generated_scene
        
        # Track output in history
        if self.history:
            self.history[-1]["output"] = final_scene
            
        return final_scene

    def evaluate_and_fix(self, scene):
        """
        Evaluates the scene and applies one round of auto-fix if needed.
        """
        eval_messages = [
            {"role": "system", "content": "You are an expert script editor."},
            {"role": "user", "content": FORMAT_VALIDATION_PROMPT.format(generated_scene=scene)}
        ]
        
        evaluation_raw = self._call_llm(eval_messages, response_format={"type": "json_object"})
        
        if not evaluation_raw:
            return scene
            
        try:
            evaluation = json.loads(evaluation_raw)
        except Exception:
            import re
            json_match = re.search(r'\{.*\}', evaluation_raw, re.DOTALL)
            if json_match:
                try:
                    evaluation = json.loads(json_match.group())
                except:
                    return scene
            else:
                return scene
                
        score = evaluation.get("format_score", 10)
        issues = evaluation.get("issues", [])
        
        logger.info(f"Scene Evaluation Score: {score}/10. Issues: {issues}")
        
        if score < 8 and issues:
            logger.info("Triggering Auto-fix...")
            fix_messages = [
                {"role": "system", "content": "You are a perfectionist script editor."},
                {"role": "user", "content": AUTO_FIX_PROMPT.format(generated_scene=scene, issues=", ".join(issues))}
            ]
            fixed_scene = self._call_llm(fix_messages)
            
            if fixed_scene.startswith("ERROR:"):
                logger.warning(f"Auto-fix failed: {fixed_scene}. Returning original.")
                return scene
                
            return fixed_scene if fixed_scene else scene
        else:
            return scene

    def iterate_scene(self, scene, iteration_type):
        """
        Applies iteration prompts like 'make it intense'.
        """
        prompts = {
            "intense": ITERATION_INTENSE_PROMPT,
            "humorous": ITERATION_HUMOROUS_PROMPT,
            "dialogue": ITERATION_DIALOGUE_ONLY_PROMPT
        }
        
        if iteration_type not in prompts:
            return "Invalid iteration type."
            
        # Add awareness of what is changing
        logger.info(f"Applying iteration: {iteration_type}")
        
        # Get language from history if possible
        language = "English"
        if self.history:
            language = self.history[-1].get("structured", {}).get("language", "English")
        
        # Format system prompt with language
        system_content = SYSTEM_PROMPT.format(language=language)
        
        # Format the specific iteration instruction
        instruction = prompts[iteration_type].format(previous_output=scene)
        
        # Include history context if available to help the model remember the previous goals
        history_context = ""
        if self.history:
            history_context = f"\nORIGINAL GOAL: {self.history[-1].get('input', 'Unknown')}\n"

        messages = [
            {"role": "system", "content": system_content + "\n\nYou are tasked with REWRITING an existing scene. You MUST NOT return the same scene twice. You MUST make significant, creative changes as requested."},
            {"role": "user", "content": f"{history_context}\n\nINSTRUCTIONS: {instruction}"}
        ]
        
        updated_scene = self._call_llm(messages)
        
        if updated_scene.startswith("ERROR:"):
            logger.warning(f"Iteration '{iteration_type}' failed: {updated_scene}")
            return updated_scene

        if not updated_scene or updated_scene.strip() == scene.strip():
            logger.warning(f"Iteration '{iteration_type}' failed or produced no change. Returning original scene.")
            return scene

        # Track iteration in history
        if self.history:
            self.history[-1][f"iteration_{iteration_type}"] = updated_scene
            
        return updated_scene

if __name__ == "__main__":
    pipeline = ScriptPipeline()
    pass
