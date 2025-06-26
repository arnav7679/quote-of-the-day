import functions_framework
import requests
import datetime
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

@functions_framework.cloud_event
def daily_quote(event):
    # Get a random quote
    response = requests.get("https://zenquotes.io/api/random")
    quote = response.json()[0]
    text = f'"{quote["q"]}"\n\n– {quote["a"]}'
    
    # Send email
    send_email("Your Daily Quote ✨", text)

    # Log to console
    now = datetime.datetime.now().isoformat()
    print(f"[{now}] Email sent: {text}")

def send_email(subject, body):
    SENDGRID_API_KEY = os.environ.get("SENDGRID_API_KEY")
    TO_EMAIL = os.environ.get("TO_EMAIL")

    if not SENDGRID_API_KEY or not TO_EMAIL:
        print("Missing SENDGRID_API_KEY or TO_EMAIL")
        return

    message = Mail(
        from_email='your_verified_sender@example.com',
        to_emails=TO_EMAIL,
        subject=subject,
        plain_text_content=body
    )

    try:
        sg = SendGridAPIClient(SENDGRID_API_KEY)
        response = sg.send(message)
        print(f"Status: {response.status_code}")
    except Exception as e:
        print(f"Error sending email: {e}")
