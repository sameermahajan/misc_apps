# app.py
import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="WhatsApp Notification Service")

client = Client(
    os.getenv("TWILIO_ACCOUNT_SID"),
    os.getenv("TWILIO_AUTH_TOKEN")
)

WHATSAPP_FROM = os.getenv("TWILIO_WHATSAPP_FROM")


class WhatsAppRequest(BaseModel):
    to: str               # e.g. +9198xxxxxxx
    message: str          # template text or session message


@app.post("/send")
def send_whatsapp(req: WhatsAppRequest):
    try:
        msg = client.messages.create(
            from_=WHATSAPP_FROM,
            to=f"whatsapp:{req.to}",
            body=req.message
        )
        return {
            "status": "sent",
            "sid": msg.sid
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
