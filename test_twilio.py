from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()  # loads .env variables

account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
client = Client(account_sid, auth_token)

try:
    message = client.messages.create(
        body="Test message",
        from_="+14176987989", # your Twilio number
        to="+919740247210"
    )
    print("Message sent:", message.sid)
except Exception as e:
    print("Error:", e)
