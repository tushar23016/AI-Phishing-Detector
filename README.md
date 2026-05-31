# AI Phishing Email Detector

An AI-powered web application that detects phishing emails using Machine Learning, Flask, and Natural Language Processing (NLP).

## Features

* AI-based phishing email detection
* Real-time email analysis
* Risk assessment and confidence score
* Dashboard with analysis history
* SQLite database integration
* Modern cybersecurity-themed UI
* Machine Learning model using TF-IDF and Logistic Regression

---

## Project Structure

```text
AI-Phishing-Detector/
│
├── app.py
├── train_model.py
├── README.md
├── requirements.txt
│
├── dataset/
│   └── phishing_emails.csv
│
├── model/
│   ├── phishing_model.pkl
│   └── vectorizer.pkl
│
├── database/
│   └── emails.db
│
├── static/
│   ├── css/
│   │   └── style.css
│   │
│   └── js/
│       └── script.js
│
└── templates/
    ├── index.html
    ├── analyze.html
    ├── result.html
    └── dashboard.html
```

---

## Technologies Used

### Frontend

* HTML5
* CSS3
* JavaScript
* Font Awesome
* Google Fonts

### Backend

* Python
* Flask

### Machine Learning

* Scikit-Learn
* TF-IDF Vectorizer
* Logistic Regression

### Database

* SQLite

---

## Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/AI-Phishing-Detector.git

cd AI-Phishing-Detector
```

---

### Create Virtual Environment

```bash
python -m venv venv
```

Activate:

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / macOS

```bash
source venv/bin/activate
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Dataset Format

The dataset must contain:

```csv
text,label
"Verify your account immediately",phishing
"Meeting scheduled tomorrow",safe
```

### Labels

* phishing
* safe

---

## Train Model

Run:

```bash
python train_model.py
```

Generated files:

```text
model/
├── phishing_model.pkl
└── vectorizer.pkl
```

---

## Run Application

```bash
python app.py
```

Open:

```text
http://127.0.0.1:5000
```

---

## Application Workflow

```text
User Input
     │
     ▼
Email Text
     │
     ▼
TF-IDF Vectorization
     │
     ▼
Machine Learning Model
     │
     ▼
Prediction
     │
     ▼
Risk Assessment
     │
     ▼
Store in Database
     │
     ▼
Dashboard
```

---

## Dashboard Features

* Total emails analyzed
* Phishing emails detected
* Safe emails detected
* Threat statistics
* Recent analysis history

---

## Deployment on Render

### Requirements

Create:

```text
requirements.txt
```

Example:

```text
Flask
pandas
scikit-learn
numpy
```

---

### Update app.py

```python
if __name__ == "__main__":

    port = int(os.environ.get("PORT", 5000))

    app.run(
        host="0.0.0.0",
        port=port
    )
```

---

### Deploy

1. Push project to GitHub
2. Create Render account
3. New Web Service
4. Connect GitHub repository
5. Deploy

Render will provide:

```text
https://your-project-name.onrender.com
```

---

## Future Improvements

* Deep Learning (LSTM/BERT)
* URL Reputation Analysis
* Attachment Scanning
* User Authentication
* Email API Integration
* PostgreSQL Database
* Advanced Threat Intelligence Dashboard
* Real-time Threat Alerts

---

## Screenshots

Add screenshots of:

* Home Page
* Analyze Page
* Result Page
* Dashboard

---

## Author

Tushar Mondal

Cybersecurity & AI Project

---

## License

This project is for educational and academic purposes.
