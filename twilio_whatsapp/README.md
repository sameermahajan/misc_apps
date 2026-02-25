# Setup

https://console.twilio.com/
    Account Dashboard -> Account SID, 
                         Auth Token

# Running app
                         
uvicorn app:app --reload --port 8000

open http://127.0.0.1:8000/docs

# Enable your device to receive whatsapp messages

console.twilio.com: Messaging → Try it out → Send a WhatsApp message -> Sandbox settings to get sandbox name
   
   Use WhatsApp and send a message from your device to
   WhatsApp number +1 415 523 8886
               join <sandbox_name>

# Send WhatsApp message from the app

Post -> Try It Out -> edit values -> Execute

# Monitoring messages

Monitor → Logs → Messaging 
