import requests
import os
from dotenv import load_dotenv

load_dotenv()

ACCESS_TOKEN = os.getenv("META_ACCESS_TOKEN")
BASE_URL = "https://graph.facebook.com/v17.0"

def send_instagram_message(recipient_id, text):
    if not ACCESS_TOKEN or "your_instagram" in ACCESS_TOKEN:
        print(f"[ERROR] Missing or invalid Meta Access Token. Cannot send message to {recipient_id}")
        return
        
    url = f"{BASE_URL}/me/messages?access_token={ACCESS_TOKEN}"
    payload = {
        "recipient": {"id": recipient_id},
        "message": {"text": text}
    }
    
    response = requests.post(url, json=payload)
    if response.status_code != 200:
        print(f"[ERROR] Meta API Error: {response.text}")
    return response.json()
