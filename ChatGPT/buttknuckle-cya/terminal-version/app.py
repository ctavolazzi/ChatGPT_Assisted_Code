# Define a function to display the game introduction and instructions
def display_intro():
  print("Welcome to the choose-your-own-adventure RPG!")
  print("In this game, you will make choices that determine the outcome of the story.")
  print("To make a choice, enter the number corresponding to the option you want to choose.")

# Define a function to start the game and display the first set of choices
def start_game():
  print("You find yourself in a dark forest, lost and alone.")
  print("1. Look for a way out of the forest")
  print("2. Try to find shelter for the night")
  print("3. Attempt to find food")
  choice = input("What would you like to do? ")

  # Handle the player's choice
  if choice == "1":
    option_1()
  elif choice == "2":
    option_2()
  elif choice == "3":
    option_3()
  else:
    print("Invalid choice. Please try again.")
    start_game()

# Define functions for each of the possible choices
def option_1():
  print("You spend hours walking, looking for a way out of the forest.")
  print("After a while, you come across a fork in the path.")
  print("1. Take the path to the left")
  print("2. Take the path to the right")
  choice = input("What would you like to do? ")

  if choice == "1":
    print("The path to the left leads you to a clearing, where you find a small cabin.")
    print("You are able to find shelter for the night and rest until morning.")
  elif choice == "2":
    print("The path to the right leads you deeper into the forest, where you become even more lost.")
    print("You eventually succumb to the elements and perish.")
  else:
    print("Invalid choice. Please try again.")
    option_1()

def option_2():
  print("You spend hours walking, looking for a place to shelter for the night.")
  print("After a while, you come across a fork in the path.")
  print("1. Take the path to the left")
  print("2. Take the path to the right")
  choice = input("What would you like to do? ")

  if choice == "1":
    print("The path to the left leads you to a clearing, where you find a small cabin.")
    print("You are able to find shelter for the night and rest until morning.")
  elif choice == "2":
    print("The path to the right leads you deeper into the forest, where you become even more lost.")
    print("You eventually succumb to the elements and perish.")
  else:
    print("Invalid choice. Please try again.")
    option_2()

def option_3():
  print("You spend hours walking, looking for food.")
  print("After a while, you come across a fork in the path.")
  print("1. Take the path to the left")
  print("2. Take the path to the right")
  choice = input("What would you like to do? ")

  if choice == "1":
    print("The path to the left leads you to a clearing, where you find a small cabin.")
    print("You are able to find shelter for the night and rest until morning.")
  elif choice == "2":
    print("The path to the right leads you deeper into the forest, where you become even more lost.")
    print("You eventually succumb to the elements and perish.")
  else:
    print("Invalid choice. Please try again.")
    option_3()

# Call the functions to start the game
display_intro()
start_game()

# Path: buttknuckle-cya/terminal-version/app.py