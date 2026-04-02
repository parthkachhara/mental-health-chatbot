def detect_risk(text):
    text = text.lower()

    crisis_keywords = [
        "want to die",
        "kill myself",
        "end my life",
        "hurt myself",
        "suicide",
        "self harm",
        "i don't want to live"
    ]

    high_keywords = [
        "hopeless",
        "worthless",
        "can't go on",
        "no reason to live",
        "give up"
    ]

    for phrase in crisis_keywords:
        if phrase in text:
            return "crisis"

    for phrase in high_keywords:
        if phrase in text:
            return "high"

    return "low"