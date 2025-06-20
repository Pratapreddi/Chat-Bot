# app.py
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

conversation_step = {}

def bot_reply(user_id, user_message):
    step = conversation_step.get(user_id, 0)

    if step == 0:
        reply = "Hello! I am your chatbot. 👋"
        conversation_step[user_id] = 1

    elif step == 1:
        reply = "Please introduce yourself to me."
        conversation_step[user_id] = 2

    elif step == 2:
        reply = f"Nice to meet you, {user_message}! Which programming language are you comfortable with — Python or Java?"
        conversation_step[user_id] = 3

    elif step == 3:
        reply = "Great choice! Are you an experienced professional or a fresher?"
        conversation_step[user_id] = 4

    elif step == 4:
        if "experience" in user_message.lower():
            reply = "Awesome! It was great talking to you. 👍"
        elif "fresher" in user_message.lower():
            reply = "Fantastic! Wishing you great success ahead! 🚀"
        else:
            reply = "Please tell me if you are experienced or a fresher."

    else:
        reply = "Thank you for chatting with me! You can refresh the page to start again."

    return reply

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_id = "user1"
    user_message = data.get("message", "")
    reply = bot_reply(user_id, user_message)
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)
