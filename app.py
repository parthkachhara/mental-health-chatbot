import streamlit as st
import pandas as pd
import re
import os

from google import genai
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

st.set_page_config(page_title="Mental Health Chatbot", page_icon="💙")

st.title("💙 AI Mental Health Support Chatbot")
st.write("This chatbot detects emotion from text and gives a supportive response.")
st.warning("Disclaimer: This chatbot provides basic emotional support only. It is not a substitute for professional mental health advice.")

# Gemini API setup
GEMINI_API_KEY = os.getenv("AIzaSyBMiInWMRd2xpWhH-PFuCrjzEKdeYqxDF0")

gemini_client = None
if GEMINI_API_KEY:
    gemini_client = genai.Client(api_key=AIzaSyBMiInWMRd2xpWhH-PFuCrjzEKdeYqxDF0)

@st.cache_data
def load_data():
    df = pd.read_csv("emotion_dataset.csv")
    return df


df = load_data()


def clean_text(text):
    text = str(text).lower()
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text


df["clean_text"] = df["text"].apply(clean_text)


@st.cache_resource
def train_model(dataframe):
    vectorizer = TfidfVectorizer(max_features=3000)

    X = vectorizer.fit_transform(dataframe["clean_text"])
    y = dataframe["emotion"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = LogisticRegression(max_iter=200)
    model.fit(X_train, y_train)

    return vectorizer, model


vectorizer, model = train_model(df)


responses = {
    "joy": "I'm glad you're feeling positive. Keep doing things that support your well-being.",
    "sadness": "I'm sorry you're feeling sad. Try talking to someone you trust and taking a little rest.",
    "anger": "It seems like you're upset. Take a pause, breathe slowly, and give yourself some time to calm down.",
    "fear": "It sounds like you're worried. Try deep breathing and focus on one step at a time.",
    "love": "That is a warm positive feeling. Staying connected with loved ones supports mental well-being."
}

# -----------------------------
# GEMINI RESPONSE GENERATOR
# -----------------------------
def generate_gemini_reply(user_input, emotion):

    if gemini_client is None:
        return None

    prompt = f"""
You are a supportive mental wellness assistant.

User message: "{user_input}"
Detected emotion: "{emotion}"

Write a short supportive response.

Rules:
- Do not diagnose mental illness
- Do not give medical advice
- Encourage calm healthy coping
- Keep the response under 80 words
"""

    try:
        response = gemini_client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text.strip()

    except:
        return None


def chatbot_reply(user_input):

    cleaned = clean_text(user_input)

    vect = vectorizer.transform([cleaned])

    emotion = model.predict(vect)[0]

    # try Gemini response
    gemini_reply = generate_gemini_reply(user_input, emotion)

    if gemini_reply:
        reply = gemini_reply
    else:
        reply = responses.get(
            emotion,
            "I'm here to support you. Please take care of yourself and talk to someone you trust."
        )

    return emotion, reply


user_input = st.text_area("Enter your message:", placeholder="Type how you are feeling...")

if st.button("Analyze"):
    if user_input.strip() == "":
        st.error("Please enter a message.")
    else:
        emotion, reply = chatbot_reply(user_input)

        st.subheader("Result")
        st.write(f"**Detected Emotion:** {emotion}")
        st.write(f"**Chatbot Response:** {reply}")