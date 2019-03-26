from flask import Flask, request, jsonify

audio_url = "https://your_domain.com/music/your_music.mp3"

app = Flask(__name__)

ncco = [
    {
        "action": "stream",
        "streamUrl": [audio_url]
    }
]

@app.route("/webhooks/answer")
def answer_call():
    return jsonify(ncco)

@app.route("/webhooks/event", methods=['POST'])
def events():
    return ("200")

if __name__ == '__main__':
    app.run(host="localhost", port=9000)
