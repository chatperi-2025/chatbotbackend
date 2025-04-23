import os
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "Welcome to the Peri Chatbot Backend!"

def get_bot_response(user_input):
    user_input = user_input.lower()
    if "hello" in user_input or "hi" in user_input:
        return "Hey there! 👋"
    elif "how are you" in user_input:
        return "I'm doing great, thanks for asking!"
    elif "your name" in user_input:
        return "I'm Peri, your friendly chatbot."
    elif "bye" in user_input:
        return "Goodbye! Take care!"
    else:
        return "I'm not sure how to respond to that."

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    message = data.get("message", "")
    response = get_bot_response(message)
    return jsonify({"response": response})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Use PORT env variable from Render
    print(f"Backend hosting is successful, running on http://0.0.0.0:{port}")
    app.run(debug=True, host="0.0.0.0", port=port)
