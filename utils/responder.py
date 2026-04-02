def generate_response(text, emotion, risk, intensity, context):
    if risk == "crisis":
        return (
            "I'm really sorry you're going through this. "
            "You deserve immediate support from a real person right now. "
            "Please contact a trusted person, local emergency services, or a crisis helpline immediately."
        )

    if risk == "high":
        return (
            "I'm really sorry you're feeling this overwhelmed. "
            "It sounds like things feel very heavy right now. "
            "Please consider reaching out to someone you trust today. "
            "You do not have to deal with this alone."
        )

    if emotion == "loneliness":
        return (
            "I'm sorry you're feeling lonely. Feeling disconnected can really hurt. "
            "Even sending a small message to one trusted person might help a little. "
            "Do you want to share what made you feel this way today?"
        )

    if emotion == "anxiety":
        return (
            "It sounds like you're feeling anxious right now. "
            "Try taking one slow breath and focusing on only the next small step. "
            "Would you like to tell me what is worrying you most?"
        )

    if emotion == "overwhelm":
        return (
            "That sounds really overwhelming. "
            "You do not have to solve everything at once. "
            "Try choosing just one small thing to focus on first. "
            "What feels like the hardest part right now?"
        )

    if emotion == "hopelessness":
        return (
            "I'm sorry you're feeling this low. "
            "When everything feels heavy, even small things can seem impossible. "
            "Please try to talk to someone you trust, even briefly. "
            "Do you want to tell me what has been weighing on you?"
        )

    if emotion == "sadness":
        return (
            "I'm sorry you're feeling sad. "
            "That can feel heavy, especially when things build up over time. "
            "Would talking about what happened today help a little?"
        )

    if emotion == "anger":
        return (
            "It sounds like something has really upset you. "
            "Taking a pause and slowing down for a moment may help before reacting. "
            "Do you want to talk about what happened?"
        )

    return (
        "I'm here with you. "
        "It sounds like you're going through something difficult. "
        "Would you like to share a little more about what is on your mind?"
    )