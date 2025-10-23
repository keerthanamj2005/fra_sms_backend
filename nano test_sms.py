from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()

account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
client = Client(account_sid, auth_token)

message = client.messages.create(
    body="Test from Flask backend!",  # <-- close the string properly
    from_="+14176987989",
    to="+918050425367"                 # <-- remove spaces in number
)

print(message.sid)
