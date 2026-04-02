import os
import pickle
import streamlit as st

from utils.safety import detect_risk
from utils.predictor import keyword_emotion_boost, detect_intensity, detect_context
from utils.responder import generate_response

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "models", "emotion_model.pkl")
VECTORIZER_PATH = os.path.join(BASE_DIR, "models", "vectorizer.pkl")


@st.cache_resource
def load_model():
    with open(MODEL_PATH, "rb") as model_file:
        model = pickle.load(model_file)

    with open(VECTORIZER_PATH, "rb") as vectorizer_file:
        vectorizer = pickle.load(vectorizer_file)

    return model, vectorizer


def predict_emotion(text, model, vectorizer):
    text_vectorized = vectorizer.transform([text])
    prediction = model.predict(text_vectorized)[0]
    return prediction


st.set_page_config(page_title="AI Mental Health Support Chatbot", page_icon="💙", layout="centered")

st.title("💙 AI Mental Health Support Chatbot")
st.write("This chatbot detects emotion from text and gives a supportive response.")

st.warning(
    "Disclaimer: This chatbot provides basic emotional support only. "
    "It is not a substitute for professional mental health advice."
)

model, vectorizer = load_model()

user_text = st.text_area("Enter your message:", placeholder="Type how you feel here...")

if st.button("Analyze"):
    if user_text.strip():
        predicted_emotion = predict_emotion(user_text, model, vectorizer)
        final_emotion = keyword_emotion_boost(user_text, predicted_emotion)
        risk = detect_risk(user_text)
        intensity = detect_intensity(user_text)
        context = detect_context(user_text)
        response = generate_response(user_text, final_emotion, risk, intensity, context)

        st.subheader("Result")
        st.write(f"**Detected Emotion:** {final_emotion}")
        st.write(f"**Intensity:** {intensity}")
        st.write(f"**Context:** {context}")
        st.write(f"**Risk Level:** {risk}")
        st.write(f"**Chatbot Response:** {response}")
    else:
        st.error("Please enter a message first.")