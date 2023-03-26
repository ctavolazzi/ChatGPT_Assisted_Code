import os
import json

def open_character():
    # Prompt the user for a folder name and file name to open
    folder_name = input("Enter the name of the folder where the character file is located: ")
    file_name = input("Enter the name of the character file to open (without the '.json' extension): ")

    # Construct the file path from the folder name and file name
    file_path = os.path.join(os.getcwd(), folder_name, f"{file_name}.json")

    # Check if the file exists
    if not os.path.exists(file_path):
        print("File not found.")
        return

    # Read and print the contents of the character file
    with open(file_path, "r") as file:
        character = json.load(file)
        print(character)