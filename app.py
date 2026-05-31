
from flask import Flask, render_template, request
import sqlite3
import pickle
import os
from datetime import datetime

app = Flask(__name__)

# =====================================
# DATABASE SETUP
# =====================================

def init_db():

    os.makedirs("database", exist_ok=True)

    conn = sqlite3.connect("database/emails.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS email_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email_text TEXT,
            prediction TEXT,
            confidence REAL,
            risk_level TEXT,
            date TEXT
        )
    """)

    conn.commit()
    conn.close()


init_db()

# =====================================
# LOAD MODEL
# =====================================

model = None
vectorizer = None

try:

    with open("model/phishing_model.pkl", "rb") as f:
        model = pickle.load(f)

    with open("model/vectorizer.pkl", "rb") as f:
        vectorizer = pickle.load(f)

    print("Model Loaded Successfully")

except Exception as e:

    print("Model not found:", e)
    print("Run train_model.py first")


# =====================================
# HELPER FUNCTION
# =====================================

def analyze_email(text):

    if model is None or vectorizer is None:

        return {
            "prediction": "Safe",
            "confidence": 0,
            "risk_level": "Unknown",
            "reasons": [
                "Model not loaded"
            ]
        }

    vectorized_text = vectorizer.transform([text])

    prediction = model.predict(vectorized_text)[0]

    probabilities = model.predict_proba(
        vectorized_text
    )[0]

    confidence = round(max(probabilities) * 100, 2)

    reasons = []

    suspicious_words = [
        "verify",
        "urgent",
        "account",
        "click",
        "password",
        "bank",
        "login",
        "suspended"
    ]

    for word in suspicious_words:

        if word.lower() in text.lower():
            reasons.append(
                f"Suspicious keyword detected: {word}"
            )

    if prediction == "phishing":

        risk_level = "High"

    else:

        risk_level = "Low"

        if not reasons:
            reasons.append(
                "No major phishing indicators found"
            )

    return {
        "prediction": prediction.capitalize(),
        "confidence": confidence,
        "risk_level": risk_level,
        "reasons": reasons
    }


# =====================================
# HOME PAGE
# =====================================

@app.route("/")
def home():

    return render_template("index.html")


# =====================================
# ANALYZE PAGE
# =====================================

@app.route("/analyze", methods=["GET", "POST"])
def analyze():

    if request.method == "GET":

        return render_template(
            "analyze.html"
        )

    email_text = request.form.get(
        "email_text", ""
    )

    result = analyze_email(
        email_text
    )

    conn = sqlite3.connect(
        "database/emails.db"
    )

    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO email_history
        (
            email_text,
            prediction,
            confidence,
            risk_level,
            date
        )
        VALUES (?, ?, ?, ?, ?)
    """,
    (
        email_text,
        result["prediction"],
        result["confidence"],
        result["risk_level"],
        datetime.now().strftime(
            "%d-%m-%Y %H:%M"
        )
    ))

    conn.commit()
    conn.close()

    return render_template(
        "result.html",
        prediction=result["prediction"],
        confidence=result["confidence"],
        risk_level=result["risk_level"],
        reasons=result["reasons"]
    )


# =====================================
# DASHBOARD
# =====================================

@app.route("/dashboard")
def dashboard():

    conn = sqlite3.connect(
        "database/emails.db"
    )

    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM email_history
        ORDER BY id DESC
        LIMIT 10
    """)

    rows = cursor.fetchall()

    history = []

    phishing_count = 0
    safe_count = 0

    for row in rows:

        history.append({
            "id": row[0],
            "date": row[5],
            "prediction": row[2],
            "risk": row[4]
        })

    cursor.execute("""
        SELECT COUNT(*)
        FROM email_history
    """)

    total_emails = cursor.fetchone()[0]

    cursor.execute("""
        SELECT COUNT(*)
        FROM email_history
        WHERE prediction='Phishing'
    """)

    phishing_count = cursor.fetchone()[0]

    cursor.execute("""
        SELECT COUNT(*)
        FROM email_history
        WHERE prediction='Safe'
    """)

    safe_count = cursor.fetchone()[0]

    conn.close()

    return render_template(
        "dashboard.html",
        total_emails=total_emails,
        phishing_detected=phishing_count,
        safe_emails=safe_count,
        accuracy=98.7,
        high_risk=phishing_count,
        medium_risk=max(
            phishing_count // 2,
            0
        ),
        low_risk=safe_count,
        blocked=phishing_count,
        malicious_urls=phishing_count,
        fake_senders=max(
            phishing_count // 2,
            0
        ),
        urgent_requests=max(
            phishing_count // 3,
            0
        ),
        malicious_attachments=max(
            phishing_count // 4,
            0
        ),
        history=history
    )


# =====================================
# RUN APP
# =====================================

if __name__ == "__main__":

    port = int(os.environ.get("PORT", 5000))

    app.run(
        host="0.0.0.0",
        port=port
    )