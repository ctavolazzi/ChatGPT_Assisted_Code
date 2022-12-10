import random

# The maximum size of a creature
MAX_SIZE = 10

# The maximum speed of a creature
MAX_SPEED = 5

# The maximum strength of a creature
MAX_STRENGTH = 5

# The maximum intelligence of a creature
MAX_INTELLIGENCE = 5

# The maximum amount of food available
MAX_FOOD = 100

class Creature:
  def __init__(self, size, speed, strength, intelligence):
    self.size = size
    self.speed = speed
    self.strength = strength
    self.intelligence = intelligence
    self.food = 0

  def __str__(self):
    # Return a string representation of the creature
    return f"Size: {self.size}, Speed: {self.speed}, Strength: {self.strength}, Intelligence: {self.intelligence}, Food: {self.food}"

  def eat(self, food_amount):
    # Eat a certain amount of food
    self.food += food_amount

class World:
  def __init__(self, size):
    self.size = size
    self.creatures = []
    self.food = MAX_FOOD

  def add_creature(self, creature):
    self.creatures.append(creature)

  def add_random_creatures(self, num_creatures):
    # Add a random number of creatures to the world
    for i in range(num_creatures):
      size = random.randint(1, MAX_SIZE)
      speed = random.randint(1, MAX_SPEED)
      strength = random.randint(1, MAX_STRENGTH)
      intelligence = random.randint(1, MAX_INTELLIGENCE)
      self.creatures.append(Creature(size, speed, strength, intelligence))

  def update(self):
    # Determine which creatures will survive and reproduce based on their attributes
    survivors = []
    for creature in self.creatures:
      # Check if the creature survives based on its attributes
      if random.random() < (creature.size / MAX_SIZE) * (creature.speed / MAX_SPEED) * (creature.strength / MAX_STRENGTH) * (creature.intelligence / MAX_INTELLIGENCE):
        survivors.append(creature)

    # Reproduce with mutations
    self.creatures = []
    for creature in survivors:
      # Create a mutated copy of the creature
      new_size = max(1, creature.size + random.randint(-1, 1))
      new_speed = max(1, creature.speed + random.randint(-1, 1))
      new_strength = max(1, creature.strength + random.randint(-1, 1))
      new_intelligence = max(1, creature.intelligence + random.randint(-1, 1))
      self.creatures.append(Creature(new_size, new_speed, new_strength, new_intelligence))

    # Allocate food to creatures
    for creature in self.creatures:
      # Calculate the amount of food the creature can eat based on its attributes
      food_amount = (creature.size / MAX_SIZE) * (creature.speed / MAX_SPEED) * (creature.strength / MAX_STRENGTH) * (creature.intelligence / MAX_INTELLIGENCE)
      # continue the function


    # Update the amount of food in the world
    self.food = max(0, self.food - len(self.creatures))

    # Check if the world is over
    if self.food == 0:
      return True

    return False

  def __str__(self):
    # Return a string representation of the world
    return f"Creatures: {self.creatures}, Food: {self.food}"

# Create a world
world = World(10)

# Add a random number of creatures to the world
world.add_random_creatures(10)

# Run the simulation


# while True:
#   # Print the world
#   print(world)

#   # Update the world
#   if world.update():
#     break

  # Wait for the user to press enter
  # input()

# Print the final world
print(world)

# Print the final creatures
print(world.creatures)

# Print the final food
print(world.food)