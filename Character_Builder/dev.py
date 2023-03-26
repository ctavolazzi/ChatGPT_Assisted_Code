# Dev environment for the app

# Overview
# 1. Define a Character class to represent the character
# 2. Define a function to interact with the user and create a new character
# 3. In the create_character function, prompt the user for the type of character they would like to create (e.g. hero, villain, sidekick)
# 4. Accept user input about the character (e.g. name, occupation, personality, backstory) and process it using the OpenAI API
# 5. Process the response from the OpenAI API and store the information about the character in a Character object
# 6. Give the user a summary of the character, including their name and characteristics
# 7. Ask the user for more input about the character (e.g. add another characteristic, modify an existing characteristic)
# 8. Repeat steps 4-7 until the user is satisfied with the character
# 9. Return the completed Character object from the create_character function
# 10. Initialize the app by calling the create_character function to create a new character, and then calling the interact_with_character function to interact with the character


# Implementation
import openai

# Set up the OpenAI API client
openai.api_key = "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"

class Character:
    def __init__(self, name):
        self.name = name
        self.characteristics = {}

    def set_characteristic(self, characteristic_name, characteristic_value):
        self.characteristics[characteristic_name] = characteristic_value

    def get_characteristic(self, characteristic_name):
        return self.characteristics.get(characteristic_name, "No such characteristic")

    def generate_response(self, prompt):
        print("Generating response...\nPrompt:", prompt)
        response = openai.Completion.create(
            engine="davinci",
            prompt=prompt,
            max_tokens=1000,
            n=1,
            stop=None,
        )
        return response.choices[0].text.strip()

    def __str__(self):
        return f"{self.name}: {self.characteristics}"


# import spacy

# # Load the English NLP model
# nlp = spacy.load("en_core_web_sm")


# def extract_characteristics(input_text):
#     doc = nlp(input_text)
#     characteristics = {}

#     # Extract the character's occupation and hobbies
#     for entity in doc.ents:
#         if entity.label_ == "OCCUPATION":
#             characteristics["occupation"] = entity.text
#         elif entity.label_ == "HOBBY":
#             characteristics["hobbies"] = entity.text

#     return characteristics


# def interact_with_character():
#     # Prompt the user for the character's name
#     character_name = input("What is your character's name? ")
#     character = Character(character_name)
#     print(f"Great! Let's create a character named {character_name}.")

#     # Prompt the user for input about the character
#     input_text = input("Tell me about your character: ")

#     # Extract the character's characteristics from the input text
#     characteristics = extract_characteristics(input_text)

#     # Update the character's characteristics with the extracted information
#     for name, value in characteristics.items():
#         character.set_characteristic(name, value)

#     # Print out the character's updated characteristics
#     print(f"{character.name}: {character.characteristics}")

#     print("Thanks for creating your character!")
#     return character



if __name__ == '__main__':
    character_name = input("Hi! I'm a blank character. What's my name? ")
    character = Character(character_name)
    interact_with_character(character)
