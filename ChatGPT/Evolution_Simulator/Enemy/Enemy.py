import random

class Enemy:
  def __init__(self, name, health, attack, defense):
    self.name = name
    self.inventory = [{'name': "health potion", 'quantity': 3}]
    self.state = {'health': health, 'attack': attack, 'defense': defense}

  def attack(self, defender):
    damage = self.state["attack"] - defender.state["defense"]
    if damage > 0:
      defender.state["health"] -= damage
      print(f"{self.name} hit {defender.name} for {damage} damage!")
    else:
      print(f"{self.name} attacked but did no damage.")

  def defend(self):
    self.state["defense"] += 5
    print(f"{self.name} increased their defense by 5.")

  def use_item(self, item):
    for i in self.inventory:
      if i["name"] == item:
        if i["quantity"] > 0:
          if item == "health potion":
            self.state["health"] += 50
            i["quantity"] -= 1
            print(f"{self.name} used a health potion and restored 50 health.")
        else:
          print(f"{self.name} does not have any {item} in their inventory.")
          break
    else:
      print(f"{self.name} does not have any {item} in their inventory.")

  def make_decision(self, enemy):
    if self.state["health"] < 50:
      if self.inventory[0]["quantity"] > 0:
        self.use_item("health potion")
      else:
        self.attack(enemy)
    else:
      if random.randint(0, 1) == 0:
        self.attack(enemy)
      else:
        self.defend()
