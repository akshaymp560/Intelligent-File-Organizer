import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB


def train_model():
    # Load dataset
    data = pd.read_csv("data/files.csv")

    X = data["filename"]
    y = data["category"]

    # Convert text → numbers
    vectorizer = CountVectorizer()
    X_vec = vectorizer.fit_transform(X)

    # Train model
    model = MultinomialNB()
    model.fit(X_vec, y)

    return model, vectorizer


def predict_category(model, vectorizer, filename):
    X = vectorizer.transform([filename])
    return model.predict(X)[0]