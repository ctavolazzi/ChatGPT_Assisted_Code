# Import necessary modules
import random

# Define game variables
health = 100
enemies = ["samurai", "ninja", "ronin"]

# Define game functions
def battle(enemy):
  global health
  print(f"You have encountered a {enemy}!")
  while health > 0:
    print("What will you do? (attack/defend)")
    action = input()
    if action == "attack":
      if random.randint(0, 1) == 0:
        print("You missed!")
      else:
        print("You hit the enemy!")
        health -= random.randint(10, 20)
        if health <= 0:
          print("You have been defeated!")
          return
    elif action == "defend":
      print("You defended against the enemy's attack!")
    else:
      print("Invalid action. Try again.")
  print("You have defeated the enemy!")

# Start the game
print("You have been transported to feudal Japan. Can you survive the challenges that await you?")
while len(enemies) > 0:
  enemy = random.choice(enemies)
  battle(enemy)
  enemies.remove(enemy)
print("You have successfully completed the game!")

# Path: ChatGPT/Evolution_Simulator/app.py
# Compare this snippet from ChatGPT/Evolution_Simulator/app.py: