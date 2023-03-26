def generate_character():
  import random
  import json
  import os

  # Generate random character information
  name = input("Enter character name: ")
  age = random.randint(18, 80)
  gender = random.choice(["male", "female", "nonbinary"])
  occupation = input("Enter character occupation: ")
  height = random.randint(150, 200)  # in cm
  weight = random.randint(50, 100)  # in kg

  # Create a dictionary of the generated character information
  character = {
      "name": name,
      "age": age,
      "gender": gender,
      "occupation": occupation,
      "physical_appearance": {
        "height": height,
        "weight": weight,
      }
  }

  # Prompt the user for a folder name to save the file in
  folder_name = input("Enter a folder name to save the character file in: ")
  folder_path = os.path.join(os.getcwd(), folder_name)

  # Create the folder if it does not already exist
  if not os.path.exists(folder_path):
    os.mkdir(folder_path)

  # Save the character as a JSON object in a file in the specified folder
  file_path = os.path.join(folder_path, "character.json")
  with open(file_path, "w") as file:
    json.dump(character, file)

  print(f"Character saved as '{file_path}'")