
import pandas as pd
import pickle
import os

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


# =====================================
# CREATE MODEL FOLDER
# =====================================

os.makedirs("model", exist_ok=True)


# =====================================
# LOAD DATASET
# =====================================

dataset_path = "dataset/phishing_emails.csv"

df = pd.read_csv(dataset_path)

print(f"Dataset Loaded: {len(df)} emails")


# =====================================
# PREPARE DATA
# =====================================

X = df["text"]
y = df["label"]

vectorizer = TfidfVectorizer(
    stop_words="english",
    max_features=5000
)

X_vectorized = vectorizer.fit_transform(X)


# =====================================
# TRAIN / TEST SPLIT
# =====================================

X_train, X_test, y_train, y_test = train_test_split(
    X_vectorized,
    y,
    test_size=0.2,
    random_state=42
)


# =====================================
# TRAIN MODEL
# =====================================

model = LogisticRegression(
    max_iter=1000
)

model.fit(X_train, y_train)


# =====================================
# TEST MODEL
# =====================================

predictions = model.predict(X_test)

accuracy = accuracy_score(
    y_test,
    predictions
)

print(f"Accuracy: {accuracy * 100:.2f}%")


# =====================================
# SAVE MODEL
# =====================================

with open(
    "model/phishing_model.pkl",
    "wb"
) as file:

    pickle.dump(
        model,
        file
    )


# =====================================
# SAVE VECTORIZER
# =====================================

with open(
    "model/vectorizer.pkl",
    "wb"
) as file:

    pickle.dump(
        vectorizer,
        file
    )


print("\nTraining Complete")
print("Model Saved: model/phishing_model.pkl")
print("Vectorizer Saved: model/vectorizer.pkl")

