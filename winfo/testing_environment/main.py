from flask import Flask, render_template, request, jsonify
import os
from dotenv import load_dotenv
from helpers.chat import chat_with_openai

load_dotenv()
API_KEY = os.environ.get("OPENAI_API_KEY")

app = Flask(__name__)

chat_history = [{"role": "system", "content": "You are a helpful assistant."}]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    global chat_history
    user_input = request.form['user_input']
    chat_history.append({"role": "user", "content": user_input})
    assistant_reply = chat_with_openai(API_KEY, chat_history)
    chat_history.append({"role": "assistant", "content": assistant_reply})
    return jsonify({'assistant_reply': assistant_reply})

if __name__ == '__main__':
    app.run(host='localhost', port=3080)
