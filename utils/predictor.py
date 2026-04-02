def keyword_emotion_boost(text, predicted_emotion):
    text = text.lower()

    if any(word in text for word in ["lonely", "alone", "isolated", "no one"]):
        return "loneliness"

    if any(word in text for word in ["anxious", "panic", "worried", "nervous"]):
        return "anxiety"

    if any(word in text for word in ["overwhelmed", "too much", "exhausted", "burnt out"]):
        return "overwhelm"

    if any(word in text for word in ["hopeless", "empty", "useless"]):
        return "hopelessness"

    return predicted_emotion


def detect_intensity(text):
    text = text.lower()

    high_intensity_words = [
        "very", "extremely", "terrible", "can't", "never",
        "completely", "so much", "too much", "really bad"
    ]

    score = sum(1 for word in high_intensity_words if word in text)

    if score >= 2:
        return "high"
    elif score == 1:
        return "medium"
    return "low"


def detect_context(text):
    text = text.lower()

    if any(word in text for word in ["exam", "study", "college", "marks", "result"]):
        return "academic stress"

    if any(word in text for word in ["friend", "friends", "ignored", "alone"]):
        return "social disconnection"

    if any(word in text for word in ["family", "mother", "father", "parents"]):
        return "family stress"

    if any(word in text for word in ["job", "career", "work"]):
        return "career stress"

    return "general emotional distress"