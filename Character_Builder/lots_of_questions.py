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


def interact_with_character():
    # Prompt the user for the character's name
    character_name = input("What is your character's name? ")
    character = Character(character_name)

    # Prompt the user for information about the character one question at a time
    questions = [
        "What is your character's age?",
        "What is your character's gender?",
        "What is your character's occupation?",
        "What is your character's height?",
        "What is your character's weight?",
        "What is your character's hair color?",
        "What is your character's eye color?",
        "What is your character's skin tone?",
        "What are your character's distinguishing features?",
        "Is your character introverted or extroverted?",
        "Is your character outgoing or reserved?",
        "Is your character kind or cruel?",
        "What other traits does your character have?",
        "What is your character's family background?",
        "Where is your character from?",
        "What is your character's education?",
        "What is your character's socio-economic status?",
        "What are your character's goals?",
        "What motivates your character?",
        "What does your character want to achieve?",
        "What are your character's strengths?",
        "What are your character's weaknesses?",
        "What challenges does your character face?",
        "Who are your character's important people?",
        "Who are your character's friends and family members?",
        "Does your character have any enemies?",
        "What events in your character's past have shaped them?",
        "What experiences have influenced your character's worldview?",
        "What conflicts does your character face in the story?",
        "What obstacles does your character have to overcome?",
        "How does your character change and grow throughout the story?",
        "What lessons does your character learn?",
        "What challenges does your character overcome?",
    ]

    for question in questions:
        response = input(question + " ")

        # prompt = f"Create a character with name {character_name} and {question} {response}"
        # api_response = character.generate_response(prompt)
        # characteristic_name, characteristic_value = api_response.split(": ")
        # characteristic_name = characteristic_name.strip().lower()
        # characteristic_value = characteristic_value.strip()
        # character.set_characteristic(characteristic_name, characteristic_value)

    # Print out the character's updated characteristics
    print(f"{character.name}: {character.characteristics}")

    print("Thanks for creating your character!")
    return character

# Run the function
interact_with_character()