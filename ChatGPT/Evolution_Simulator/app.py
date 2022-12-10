# Import necessary modules
import random
# from Enemy import Enemy

# Define game variables
player_name = "Player"
player_health = 100
player_attack = 10
player_defense = 5

enemy_name = "Enemy"
enemy_health = 100
enemy_attack = 10
enemy_defense = 5

# Define game functions
def attack(attacker, defender):
  damage = attacker["attack"] - defender["defense"]
  if damage > 0:
    defender["health"] -= damage
    print(f"{attacker['name']} hit {defender['name']} for {damage} damage!")
  else:
    print(f"{attacker['name']} attacked but did no damage.")

def defend(defender):
  defender["defense"] += 5
  print(f"{defender['name']} increased their defense by 5.")

def get_input():
  print("What will you do? (attack/defend/quit)")
  return input()

# Start the game
player = {"name": player_name, "health": player_health, "attack": player_attack, "defense": player_defense}

enemy = {"name": enemy_name, "health": enemy_health, "attack": enemy_attack, "defense": enemy_defense}

print(f"Welcome to the game, {player_name}! You are fighting against {enemy_name}.")

while player_health > 0 and enemy_health > 0:
  action = get_input()
  if action == "attack":
    attack(player, enemy)
    if enemy_health > 0:
      attack(enemy, player)
  elif action == "defend":
    defend(player)
    if enemy_health > 0:
      attack(enemy, player)
  elif action == "quit":
    print("Thanks for playing!")
    break
  else:
    print("Invalid action. Try again.")

if player_health > 0:
  print(f"Congratulations, {player_name}! You have defeated {enemy_name}!")
else:
  print(f"Sorry, {player_name}. You were defeated by {enemy_name}. Better luck next time.")
