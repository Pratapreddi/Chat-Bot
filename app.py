# app.py
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Track conversation state
conversation_step = {}

def bot_reply(user_id, user_message):
    step = conversation_step.get(user_id, 0)

    if step == 0:
        reply = "Hello! 👋 Welcome to our Voice ChatBot."
        conversation_step[user_id] = 1

    elif step == 1:
        reply = "I am your here to interact with you! 😊 Could you please tell me your name?"
        conversation_step[user_id] = 2

    elif step == 2:
        reply = f"Nice to meet you, {user_message}! Which language are you comfortable with? Do you know Java or Python?"
        conversation_step[user_id] = 3

    elif step == 3:
        reply = "Good to know! Are you an experienced professional or a fresher?"
        conversation_step[user_id] = 4

    elif step == 4:
        if "experience" in user_message.lower():
            reply = "Great! How many years of experience do you have, and in what role?"
            conversation_step[user_id] = 5
        elif "fresher" in user_message.lower():
            reply = "Awesome! What role are you seeking, and which programming language are you perfect in?"
            conversation_step[user_id] = 6
        else:
            reply = "Please tell me if you are experienced or a fresher."

    elif step == 5:
        reply = f"Thank you! You have {user_message}. Wishing you all the best in your career journey! 🚀"
        conversation_step[user_id] = 7

    elif step == 6:
        reply = f"Fantastic! You're aiming for {user_message}. Keep learning and growing! 🌟"
        conversation_step[user_id] = 7

    else:
        reply = "Thank you for chatting with me! If you want to restart, please refresh the page."

    return reply

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_id = "user1"  # Simplified user ID
    user_message = data.get("message", "")
    reply = bot_reply(user_id, user_message)
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)
