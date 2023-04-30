import os
from dotenv import load_dotenv
from Helpers.chat import chat_with_openai

load_dotenv()
API_KEY = os.environ.get("OPENAI_API_KEY")

def app(API_KEY):
    print("Welcome to the OpenAI chatbot!")
    print("Type 'quit' to exit the program.")
    print("Type 'reset' to reset the chatbot.")
    print("Type 'help' to see a list of commands.")

    chat_array = [{"role": "system", "content": "You are a helpful assistant."}]

    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            break
        elif user_input.lower() == "reset":
            chat_array = [{"role": "system", "content": "You are a helpful assistant."}]
            print("Chatbot has been reset.")
        elif user_input.lower() == "help":
            print("Type 'quit' to exit the program.")
            print("Type 'reset' to reset the chatbot.")
            print("Type 'help' to see a list of commands.")
        else:
            chat_array.append({"role": "user", "content": user_input})
            assistant_reply = chat_with_openai(API_KEY, chat_array)
            print("Chatbot:", assistant_reply)
            chat_array.append({"role": "assistant", "content": assistant_reply})

if __name__ == "__main__":
    app(API_KEY)
