from flask import Flask, request, jsonify
import requests, time

app = Flask(__name__)

URL = "https://api.pavlok.com/api/v5/stimulus/send"
HEADERS = {
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6bnVsbCwiaWQiOjM2MjQ2MiwiZW1haWwiOiJwcmlsZXk1MTExOUBnbWFpbC5jb20iLCJpc19hcHBsaWNhdGlvbiI6ZmFsc2UsImV4cCI6MTc5NDE3MjE1MSwic3ViIjoiYWNjZXNzIn0.tYs16o2vGRRHeu0aX5UnPMs-DdmTVNYXOqpA3853z5U",
    "accept": "application/json",
    "Content-Type": "application/json"
}

def send_vibe(val=100):
    payload = {"stimulus": {"stimulusType": "vibe", "stimulusValue": val}}
    requests.post(URL, headers=HEADERS, json=payload)
    time.sleep(2)

def send_beep(val=20):
    payload = {"stimulus": {"stimulusType": "beep", "stimulusValue": val}}
    requests.post(URL, headers=HEADERS, json=payload)
    time.sleep(2)

@app.route("/babyalert", methods=["POST"])
def baby_alert():
    for i in range(1, 15):
        send_vibe(100)
        if i % 7 == 0:
            send_beep(20)
    return jsonify({"message": "Vibration pattern complete"})

@app.route("/")
def home():
    return "Pavlok Baby-Alert Webhook is live."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
