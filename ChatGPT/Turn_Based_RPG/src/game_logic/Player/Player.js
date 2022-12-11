import React from 'react';

class Player extends React.Component {
  constructor({ name, initialHealth, initialInventory }) {
    super();
    this.name = name;
    this.health = initialHealth;
    this.inventory = initialInventory;
  }

  // Method to attack the enemy
  attack(enemy) {
    enemy.health -= 10;
  }

  // Method to defend against the enemy's attack
  defend() {
    this.health -= 5;
  }

  // Method to use an item from the player's inventory
  useItem(item) {
    if (this.inventory.length > 0) {
      if (item === 'health potion') {
        this.health += 20;
      }
      // Remove the used item from the player's inventory
      this.inventory = this.inventory.filter(i => i !== item);
    }
  }
}

export default Player;
