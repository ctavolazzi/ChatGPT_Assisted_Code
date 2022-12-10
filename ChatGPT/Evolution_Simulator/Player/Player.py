from Enemy.Enemy import Enemy

class Player(Enemy):
  def __init__(self, name, health, attack, defense):
    super().__init__(name, health, attack, defense)
    self.inventory = {"name": "health potion", "quantity": 3}

  def make_decision(self, enemy):
    print("What will you do? (attack/defend/use item)")
    action = input()
    if action == "attack":
      self.attack(enemy)
    elif action == "defend":
      self.defend()
    elif action == "use item":
      print("What item do you want to use?")
      item = input()
      self.use_item(item)
    else:
      print("Invalid action. Try again.")