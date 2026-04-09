from genre_presets import get_genre_style

def build_script_prompt(topic, genre, tone, characters, context, memory):

    style = get_genre_style(genre)

    return f"""
You are an elite screenplay writer.

STYLE:
{style}

TONE:
{tone}

CHARACTER MEMORY:
{memory}

PREVIOUS SCENES:
{context}

CHARACTERS:
{characters}

TASK:
Continue the story and write the NEXT SCENE.

STRICT FORMAT:
- Scene heading (INT./EXT.)
- Character names in ALL CAPS
- Dialogues properly formatted
- No explanations

SCENE IDEA:
{topic}
"""