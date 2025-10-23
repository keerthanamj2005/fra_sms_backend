from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()

account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
from_number = os.getenv("TWILIO_FROM")
to_number = "+919740247210"  # VERIFIED number

client = Client(account_sid, auth_token)

try:
    message = client.messages.create(
        body="Test message from Flask backend!",
        from_=from_number,
        to=to_number
    )
    print("Message sent! SID:", message.sid)
except Exception as e:
    print("Error sending SMS:", e)
