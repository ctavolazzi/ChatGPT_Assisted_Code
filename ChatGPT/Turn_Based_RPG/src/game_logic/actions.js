

// Attack the enemy, reducing their health
export const attack = (enemyHealth, setEnemyHealth) => {
  setEnemyHealth(enemyHealth - 10);
};

// Defend against the enemy's attack, reducing the damage taken
export const defend = (playerHealth, setPlayerHealth) => {
  setPlayerHealth(playerHealth - 5);
};

// Use an item from the player's inventory, if available
export const activateItem = (playerHealth, setPlayerHealth, playerInventory, setPlayerInventory) => {
  if (playerInventory.length > 0) {
    const item = playerInventory[0];
    if (item === 'health potion') {
      setPlayerHealth(playerHealth + 20);
    }
    // Remove the used item from the player's inventory
    setPlayerInventory(playerInventory.slice(1));
  }
};