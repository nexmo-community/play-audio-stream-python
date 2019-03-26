from flask import Flask, request, jsonify
import nexmo

audio_url = "https://your_domain.com/music/your_music.mp3"

APPLICATION_ID = "YOUR_APP_ID"
PRIVATE_KEY = "private.key"
CONF_NAME = "Soothing Conference"

uuid = ""

ncco = [
    {
        "action": "talk",
        "text": "Please wait while we connect you to the conference"
    },
    {
        "action": "conversation",
        "name": CONF_NAME
    }
]

app = Flask(__name__)

@app.route("/webhooks/answer")
def answer_call():
    global uuid, in_conf
    uuid = request.args['uuid']
    print("UUID:====> %s" % uuid)
    return (jsonify(ncco))

@app.route("/webhooks/event", methods=['POST'])
def events():
    return ("200")

@app.route("/stream")
def stream():
    client = nexmo.Client(application_id = APPLICATION_ID, private_key=PRIVATE_KEY)
    client.send_audio(uuid, stream_url=[audio_url])
    return ("200")

if __name__ == '__main__':
    app.run(host="localhost", port=9000)

