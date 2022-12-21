# Define a global dictionary to store the player's choices
choices = {}

# Define a dictionary to map the player's choices to the appropriate output
outputs = {
    "start": {
        1: "You spend hours walking, looking for a way out of the forest.",
        2: "You spend hours walking, looking for a place to shelter for the night.",
        3: "You spend hours walking, looking for food."
    },
    "left": {
        1: "The path to the left leads to a river.",
        2: "The path to the left leads to a cave.",
        3: "The path to the left leads to a house."
    },
    "right": {
        1: "The path to the right leads to a river.",
        2: "The path to the right leads to a cave.",
        3: "The path to the right leads to a house."
    },
    "river": {
        1: "You drink the water from the river.",
        2: "You swim across the river.",
        3: "You build a raft to cross the river."
    },
    "cave": {
        1: "You enter the cave.",
        2: "You climb the cave.",
        3: "You dig under the cave."
    },
    "house": {
        1: "You enter the house.",
        2: "You climb the house.",
        3: "You dig under the house."
    },
    "quit": {
        1: "Thanks for playing!"
    }
}

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
def handle_choice(path, choice):
  # Add the player's choice to the choices dictionary
  choices[path] = choice
  # Check if the player has reached the end of the game
  if path == "house" and choice == "1":
    end_game("win")
  elif path == "cave" and choice == "2":
    end_game("lose")
  # Check if the player has reached a dead end
  elif path == "river" and choice == "1":
    end_game("lose")
  # Check if the player has reached a fork in the road
  elif path in ["start", "left", "right"]:
    handle_fork(path)
  # Otherwise, the player must be at a river, cave, or house
  elif path == "quit":
    print("Thanks for playing!")
  else:
    handle_path(path)

# Define a function to handle the player's choice at a fork in the road
def handle_fork(path):
  print("You come to a fork in the road.")
  print("To the left is a path.")
  print("To the right is another path.")

  # Get the user's choice
  choice = input("Which path will you take? (Enter 1 for left or 2 for right)")

  # Handle the choice
  if choice == "1":
    handle_choice("left", path)
  elif choice == "2":
    handle_choice("right", path)
  elif choice == "quit":
    print("Thanks for playing!")
  else:
    print("That is not a valid choice. Please try again.")
    handle_fork(path)


# Define a function to handle the player's choice at a river, cave, or house
def handle_path(path):
  print(outputs[path][int(choices[path])])
  print("1. Go back the way you came.")
  if path == "river":
    print("2. Look for another way out of the forest.")
    print("3. Try to find shelter for the night.")
  elif path == "cave":
    print("2. Look for another way out of the forest.")
    print("3. Attempt to find food.")
  elif path == "house":
    print("2. Look for another way out of the forest.")
    print("3. Try to find shelter for the night.")
  choice = input("What would you like to do? ")
  if choice == "1":
    handle_choice(path, choice)
  elif choice == "2":
    handle_choice("start", choice)
  elif choice == "3":
    handle_choice(path, choice)
  elif choice == "quit":
    print("Thanks for playing!")
  else:
    print("That is not a valid choice.")
    handle_path(path)

# Define a function to end the game
def end_game(outcome):
  if outcome == "win":
    print("You found your way out of the forest!")
  elif outcome == "lose":
    print("You died of starvation!")
  print("Thanks for playing!")

# Call the display_intro() function
display_intro()

# Call the start_game() function
start_game()

# Path: buttknuckle-cya/terminal-version/app.py