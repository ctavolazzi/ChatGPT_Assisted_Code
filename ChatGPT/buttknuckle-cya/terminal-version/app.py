# Define a global dictionary to store the player's choices
choices = {}

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
  handle_choice("start", choice)

# Define a function to handle the player's choice
def handle_choice(key, choice):
  # Store the choice in the dictionary
  choices[key] = choice

  # Check if the choice is valid
  if not choice.isdigit():
    print("Invalid choice. Please enter a number.")
    return

  choice = int(choice)

  # Handle the player's choice based on the current game state
  if key == "start":
    if choice == 1:
      print("You spend hours walking, looking for a way out of the forest.")
    elif choice == 2:
      print("You spend hours walking, looking for a place to shelter for the night.")
    elif choice == 3:
      print("You spend hours walking, looking for food.")
    else:
      print("Invalid choice. Please try again.")
      start_game()
  elif key == "left":
    if choice == 1:
      print("The path to the left leads to a river.")
    elif choice == 2:
      print("The path to the left leads to a cave.")
    elif choice == 3:
      print("The path to the left leads to a house.")
    else:
      print("Invalid choice. Please try again.")
      handle_choice("left", input("What would you like to do? "))
  elif key == "right":
    if choice == 1:
      print("The path to the right leads to a river.")
    elif choice == 2:
      print("The path to the right leads to a cave.")
    elif choice == 3:
      print("The path to the right leads to a house.")
    else:
      print("Invalid choice. Please try again.")
      handle_choice("right", input("What would you like to do? "))
  elif key == "river":
    if choice == 1:
      print("You drink the water from the river.")
    elif choice == 2:
      print("You swim across the river.")
    elif choice == 3:
      print("You build a raft to cross the river.")
    else:
      print("Invalid choice. Please try again.")
      handle_choice("river", input("What would you like to do? "))
  elif key == "cave":
    if choice == 1:
      print("You enter the cave.")
    elif choice == 2:
      print("You climb the cave.")
    elif choice == 3:
      print("You dig under the cave.")
    else:
      print("Invalid choice. Please try again.")
      handle_choice("cave", input("What would you like to do? "))
  elif key == "house":
    if choice == 1:
      print("You enter the house.")
    elif choice == 2:
      print("You climb the house.")
    elif choice == 3:
      print("You dig under the house.")
    else:
      print("Invalid choice. Please try again.")
      handle_choice("house", input("What would you like to do? "))
  else:
    print("Invalid choice. Please try again.")
    # start_game()

#start the game
display_intro()
start_game()

# Display the player's choices
print("You have made the following choices:")
for key, value in choices.items():
  print(key, value)

# The output of the program is:
# Welcome to the choose-your-own-adventure RPG!
# In this game, you will make choices that determine the outcome of the story.
# To make a choice, enter the number corresponding to the option you want to choose.
# You find yourself in a dark forest, lost and alone.
# 1. Look for a way out of the forest
# 2. Try to find shelter for the night
# 3. Attempt to find food
# What would you like to do?

# And the player continues making choices from there