class Enemy {
  constructor(name, initialHealth, initialInventory) {
    this.name = name;
    this.health = initialHealth;
    this.inventory = initialInventory;
  }

  attack(player) {
    player.health -= 10;
  }

  defend() {
    this.health -= 5;
  }

  useItem(item) {
    if (this.inventory.length > 0) {
      if (item === 'health potion') {
        this.health += 20;
      }
      // Remove the used item from the enemy's inventory
      this.inventory = this.inventory.filter(i => i !== item);
    }
  }
}

export default Enemy;
