import os
import pickle
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "data", "emotion_dataset.csv")
MODEL_PATH = os.path.join(BASE_DIR, "models", "emotion_model.pkl")
VECTORIZER_PATH = os.path.join(BASE_DIR, "models", "vectorizer.pkl")


def main():
    df = pd.read_csv(DATA_PATH)

    # Change these column names if your dataset uses different ones
    text_column = "text"
    label_column = "emotion"

    X = df[text_column].astype(str)
    y = df[label_column].astype(str)

    vectorizer = TfidfVectorizer()
    X_vectorized = vectorizer.fit_transform(X)

    model = LogisticRegression(max_iter=1000)
    model.fit(X_vectorized, y)

    with open(MODEL_PATH, "wb") as model_file:
        pickle.dump(model, model_file)

    with open(VECTORIZER_PATH, "wb") as vectorizer_file:
        pickle.dump(vectorizer, vectorizer_file)

    print("Model and vectorizer saved successfully.")


if __name__ == "__main__":
    main()