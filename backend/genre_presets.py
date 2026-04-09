def get_genre_style(genre):
    styles = {
        "hollywood": "cinematic, sharp dialogue, realistic pacing",
        "bollywood": "dramatic, emotional, expressive dialogues, family themes",
        "kdrama": "slow-burn emotions, subtle tension, romantic depth",
        "anime": "stylized action, exaggerated emotions, internal monologue",
    }

    return styles.get(genre.lower(), "cinematic storytelling")