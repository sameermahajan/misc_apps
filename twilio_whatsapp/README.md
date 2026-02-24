https://console.twilio.com/
    Account Dashboard -> Account SID, 
                         Auth Token
                         
uvicorn app:app --reload --port 8000

open http://127.0.0.1:8000/docs

console.twilio.com: Messaging → Try it out → Send a WhatsApp message -> Sandbox settings to get sandbox name
   Use WhatsApp and send a message from your device to
   WhatsApp number +1 415 523 8886
               join <sandbox_name>

Post -> Try It Out -> edit values -> Execute
