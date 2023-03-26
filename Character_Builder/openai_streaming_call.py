import requests
import json
import sseclient
import os

from character_generator import generate_character
from open_character import open_character

API_KEY = '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'

history = {
    'previous_prompts': [],
    'previous_responses': []
}

def perform_request(prompt, history):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {API_KEY}'
    }

    data = {
        'model': 'text-davinci-002',
        'prompt': prompt,
        'temperature': 0.5,
        'max_tokens': 150,
        'top_p': 1,
        'frequency_penalty': 0,
        'presence_penalty': 0
    }

    response = requests.post('https://api.openai.com/v1/chat/completions', headers=headers, data=json.dumps(data))

    if response.status_code != 200:
        print('Error:', response.json()['error'])
        return

    # Get the model-generated message from the response
    message = response.json()['messages'][-1]['text']

    # Print the message and add it to the history of previous responses
    print(f"AI: {message}")
    history['previous_responses'].append(f"AI: {message}")

if __name__ == '__main__':
    escape_words = ['exit', 'quit', 'q', 'character', 'open character']

    #generate_character()

    while True:

        user_input = input("\nPrompt: ").lower().strip()

        # Check if the user wants to open a character file
        if user_input.startswith('open character'):
            open_character()
            continue

        # print("History: ", history)

        for word in escape_words:
            if word == user_input:
                exit()

        # Add the user input to the history of previous prompts
        history['previous_prompts'].append(user_input)

        # Concatenate the previous prompts and responses into a single prompt
        prompt = '\n'.join(history['previous_prompts'] + history['previous_responses']) + '\n'

        # Send the prompt to the OpenAI API and get a response
        perform_request(prompt, history)



#def performRequestWithStreaming(prompt, history):

    # TODO: Add a way to search through the history of previous prompts and responses first before sending a request to the API.
    # TODO: Add a way to process the history of previous prompts and responses before sending a request to the API.
    # TODO: Add a way to save the history of previous prompts and responses to a file.
    # TODO: Add a way to load the history of previous prompts and responses from a file.
    # TODO: Add a way to save the history of previous prompts and responses to a database.
    # TODO: Add a way to load the history of previous prompts and responses from a database.

    reqUrl = 'https://api.openai.com/v1/completions'
    reqHeaders = {
        'Accept': 'text/event-stream',
        'Authorization': 'Bearer ' + API_KEY
    }
    reqBody = {
      "model": "text-davinci-003",
      "prompt": prompt,
      "max_tokens": 4096,
      "temperature": 0,
      "stream": True,
    }
    request = requests.post(reqUrl, stream=True, headers=reqHeaders, json=reqBody)

    # history['previous_responses'].append(request.text)
    response_text = ''

    client = sseclient.SSEClient(request)

    for event in client.events():
        if event.data != '[DONE]':
            response_text += json.loads(event.data)['choices'][0]['text']
            print(json.loads(event.data)['choices'][0]['text'], end="", flush=True),
        else:
            history['previous_responses'].append(response_text)
            print('\n')
            break

#if __name__ == '__main__':
    escape_words = ['exit', 'quit', 'q', 'character']

    while True:
        user_input = input("\nPrompt: ").lower().strip()

        for word in escape_words:
            if word == user_input:
                exit()

        if user_input == "wikipedia":
            print("fetching info from Wikipedia")
            continue

        if user_input == 'make character':
            generate_character()
            continue

        if user_input == 'open character':
            open_character()

        # if user_input == 'scan character':
        #     # Read and print the character file contents
        #     file_path = os.path.join(folder_path, "character.json")
        #     with open(file_path, "r") as file:
        #         character = json.load(file)
        #         print(character)

        history['previous_prompts'].append(user_input)

        performRequestWithStreaming(user_input, history)
