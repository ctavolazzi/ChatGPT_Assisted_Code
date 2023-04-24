from flask import Flask, request, jsonify
import openai
import os
import subprocess

app = Flask(__name__)

openai.api_key = os.getenv('OPENAI_API_KEY')
model_engine = "text-davinci-002"

# Post a message
@app.route('/api/openai', methods=['POST'])
def openai_api():
    prompt = request.json['message']

    if not prompt:
        return jsonify({
            'status': 'error',
            'message': 'Invalid prompt.'
        })

    try:
        response = openai.Completion.create(
            engine=model_engine,
            prompt=prompt,
            max_tokens=150,
            n=1,
            stop=None,
            temperature=0.7,
        )
        message = response.choices[0].text.strip()

        return jsonify({
            'status': 'success',
            'data': message
        })
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        })

# Handle user message
@app.route('/api/message', methods=['POST'])
def handle_message():
    user_message = request.json['message']

    # Call OpenAI API to get response
    response = openai.Completion.create(
        engine=model_engine,
        prompt=user_message,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.7,
    )

    ai_message = response.choices[0].text.strip()

    # Save user message and AI response to a file
    with open('conversation.txt', 'a') as f:
        f.write(f"User: {user_message}\n")
        f.write(f"AI: {ai_message}\n\n")

    return jsonify({'message': ai_message})

# Get the conversation history
@app.route('/api/conversation', methods=['GET'])
def get_conversation():
    with open('conversation.txt', 'r') as f:
        conversation = f.read()
    return jsonify({'conversation': conversation})

if __name__ == '__main__':
    subprocess.Popen(["npm", "start"], cwd="/Users/ctavolazzi/Code/winfo/sandbox/react_chatbot/src")
    app.run(debug=True, port=5000)
