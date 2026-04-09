import chromadb

client = chromadb.Client()

scene_collection = client.get_or_create_collection("scenes")
character_collection = client.get_or_create_collection("characters")


# -------- SCENES --------
def store_scene(scene_text):
    scene_collection.add(
        documents=[scene_text],
        ids=[str(hash(scene_text))]
    )


def get_scene_context(query):
    results = scene_collection.query(
        query_texts=[query],
        n_results=3
    )
    return " ".join(results["documents"][0]) if results["documents"] else ""


# -------- CHARACTERS --------
def store_characters(characters):
    character_collection.add(
        documents=[characters],
        ids=[str(hash(characters))]
    )


def get_character_memory():
    results = character_collection.get()
    return " ".join(results["documents"]) if results["documents"] else ""