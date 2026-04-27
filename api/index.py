from fastapi import FastAPI, Request, Depends
from sqlalchemy.orm import Session
import os
import json
from .database import SessionLocal, Machine, UserState, init_db
from .gemini_service import get_gemini_response
from .meta_service import send_instagram_message
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

# Initialize DB on startup
@app.on_event("startup")
def startup():
    init_db()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/api/webhook")
def verify_webhook(request: Request):
    verify_token = os.getenv("META_VERIFY_TOKEN")
    params = request.query_params
    mode = params.get("hub.mode")
    token = params.get("hub.verify_token")
    challenge = params.get("hub.challenge")

    if mode == "subscribe" and token == verify_token:
        return int(challenge)
    return {"error": "Verification failed"}

@app.post("/api/webhook")
async def handle_webhook(request: Request, db: Session = Depends(get_db)):
    data = await request.json()
    
    if data.get("object") == "instagram":
        for entry in data.get("entry", []):
            for messaging_event in entry.get("messaging", []):
                if messaging_event.get("message"):
                    sender_id = messaging_event["sender"]["id"]
                    message_text = messaging_event["message"].get("text", "")

                    if message_text:
                        # 1. Get Machines from DB
                        machines = [m.name for m in db.query(Machine).all()]
                        
                        # 2. Get/Update User State
                        user_state = db.query(UserState).filter(UserState.user_id == sender_id).first()
                        history = ""
                        if user_state:
                            history = user_state.state_data
                        
                        # 3. Get Gemini Response
                        ai_response = await get_gemini_response(message_text, machines, history)
                        
                        # 4. Update History (keep it short to save tokens)
                        new_history = f"User: {message_text}\nBot: {ai_response}"
                        if user_state:
                            user_state.state_data = new_history[-500:] # Keep last 500 chars
                        else:
                            db.add(UserState(user_id=sender_id, state_data=new_history))
                        db.commit()
                        
                        # 5. Send Message back
                        send_instagram_message(sender_id, ai_response)

    return {"status": "ok"}
