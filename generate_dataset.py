import pandas as pd
import random

phishing_templates = [
    "Your account has been suspended. Verify immediately.",
    "Click here to update your password.",
    "Urgent action required to secure your account.",
    "Your bank account requires verification.",
    "Claim your prize now.",
    "Your PayPal account has been limited.",
    "Security alert detected on your account.",
    "Update your billing information immediately.",
    "Your package is waiting for confirmation.",
    "Verify your identity to avoid suspension."
]

safe_templates = [
    "Meeting scheduled for tomorrow.",
    "Please review the attached report.",
    "Thank you for your purchase.",
    "Project discussion at 2 PM.",
    "Your interview is confirmed.",
    "Happy birthday and best wishes.",
    "The team meeting starts at 10 AM.",
    "Please find the invoice attached.",
    "Your order has been shipped.",
    "Class has been rescheduled."
]

data = []

# 500 phishing emails
for _ in range(1000):
    data.append([random.choice(phishing_templates), "phishing"])

# 500 safe emails
for _ in range(1000):
    data.append([random.choice(safe_templates), "safe"])

df = pd.DataFrame(data, columns=["text", "label"])

df.to_csv("dataset/phishing_emails.csv", index=False)

print("Dataset created successfully!")
print("Total emails:", len(df))