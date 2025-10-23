from flask import Flask, request, jsonify
from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv()
app = Flask(__name__)

# Twilio setup
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
from_number = os.getenv("TWILIO_FROM")
client = Client(account_sid, auth_token)

# --- Mock Yojana logic ---
def check_yojana(category, land_index):
    """
    Example rule-based logic (replace with AI model later)
    """
    if category.lower() == "st":
        return "Forest Dwellers Empowerment Yojana"
    elif category.lower() == "sc":
        return "Pradhan Mantri Van Dhan Yojana"
    elif land_index < 3:
        return "Land Development Grant"
    else:
        return "General FRA Benefit"

# --- API Endpoint ---
@app.route('/send_sms', methods=['POST'])
def send_sms():
    data = request.get_json()
    phone = data.get("phone")
    category = data.get("category")
    land_index = data.get("land_index")

    if not phone or category is None or land_index is None:
        return jsonify({"error": "Missing required fields"}), 400

    # Decide Yojana
    yojana = check_yojana(category, land_index)

    # Message text
    body = f"Dear Farmer, based on your land index {land_index}, you are eligible for {yojana}. Visit your local FRA office for details."

    try:
        message = client.messages.create(
            body=body,
            from_=from_number,
            to=phone
        )
        return jsonify({
            "status": "sent",
            "sid": message.sid,
            "yojana": yojana
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

	
