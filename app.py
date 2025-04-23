from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # This allows cross-origin requests from the frontend

# Route for the home page
@app.route("/")
def home():
    return "Welcome to the Peri Chatbot Backend!"

# Function to process the chatbot's response
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

# Route to handle chat messages
@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()  # Get the JSON data sent from frontend
    message = data.get("message", "")  # Extract the user message
    response = get_bot_response(message)  # Get the bot's response
    return jsonify({"response": response})  # Send back the response as JSON

if __name__ == "__main__":
    print("Backend hosting is successful, running on http://127.0.0.1:5000")
    app.run(debug=True)
