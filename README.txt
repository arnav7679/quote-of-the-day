
🌞 Quote of the Day — Serverless Email Scheduler (GCP + Python + SendGrid)

This project uses Google Cloud Functions, Pub/Sub, and Cloud Scheduler to automatically send a random inspirational quote to your email every day — completely serverless and scalable.

> "When asked, how do you write? I invariably answer, one word at a time." – Stephen King

==============================
🧰 Tech Stack
==============================
- Python 3.10
- Google Cloud Functions (Event-Driven)
- Google Cloud Pub/Sub
- Google Cloud Scheduler
- SendGrid Email API
- ZenQuotes API (https://zenquotes.io/api/random)

==============================
📁 Project Structure
==============================
quote-of-the-day-gcp/
├── main.py               # Cloud Function logic
├── requirements.txt      # Python dependencies
└── README.txt            # Project documentation

==============================
⚙️ Setup Instructions
==============================
1. Prerequisites
------------------------------
- A Google Cloud Platform (GCP) project
- gcloud SDK installed & authenticated
- A free SendGrid account (https://sendgrid.com)
- Verified sender email in SendGrid

2. Create and Activate GCP Project
----------------------------------
gcloud auth login
gcloud config set project your-project-id

3. Prepare Your Files
------------------------------
main.py:
[ See your code for full main.py content ]

requirements.txt:
requests
functions-framework
sendgrid

4. Create Pub/Sub Topic
------------------------------
gcloud pubsub topics create quote-scheduler

5. Deploy the Function
------------------------------
gcloud functions deploy daily_quote ^
  --runtime python310 ^
  --trigger-topic=quote-scheduler ^
  --region=us-central1 ^
  --set-env-vars SENDGRID_API_KEY=YOUR_KEY,TO_EMAIL=youremail@example.com

6. Create the Cloud Scheduler Job
----------------------------------
gcloud scheduler jobs create pubsub quote-scheduler-job ^
  --schedule="0 9 * * *" ^
  --time-zone="Asia/Kolkata" ^
  --topic=quote-scheduler ^
  --message-body="{}" ^
  --location=us-central1

7. Manually Test the Function
------------------------------
gcloud pubsub topics publish quote-scheduler --message="{}"

==============================
✅ Output
==============================
You should receive an email daily at 9:00 AM IST containing a random inspirational quote.

Check logs using:
gcloud functions logs read daily_quote --region=us-central1 --limit=10

==============================
🔒 Security Tips
==============================
- Never commit your SendGrid API key to GitHub!
- Use environment variables instead of hardcoded credentials
- Use Google Secret Manager for better security (optional)

==============================
📬 Credits
==============================
- Quote API: https://zenquotes.io
- Email: SendGrid (https://sendgrid.com)

==============================
📄 License
==============================
MIT License. Free to use.
