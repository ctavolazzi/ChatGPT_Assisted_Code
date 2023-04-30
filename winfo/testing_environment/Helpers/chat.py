import openai

def chat_with_openai(api_key, messages):
    openai.api_key = api_key
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    assistant_reply = response['choices'][0]['message']['content']
    return assistant_reply
