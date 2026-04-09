from fastapi import FastAPI
from pydantic import BaseModel
import openai

from prompt_engine import build_script_prompt
from vector_store import (
    store_scene,
    get_scene_context,
    store_characters,
    get_character_memory,
)

app = FastAPI()

openai.api_key = "YOUR_OPENAI_API_KEY"


class ScriptRequest(BaseModel):
    topic: str
    genre: str
    tone: str
    characters: str


@app.post("/generate")
def generate_script(req: ScriptRequest):

    # Store characters once
    store_characters(req.characters)

    # Retrieve memory
    scene_context = get_scene_context(req.topic)
    character_memory = get_character_memory()

    prompt = build_script_prompt(
        req.topic,
        req.genre,
        req.tone,
        req.characters,
        scene_context,
        character_memory
    )

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.9
    )

    scene = response["choices"][0]["message"]["content"]

    store_scene(scene)

    return {"scene": scene}