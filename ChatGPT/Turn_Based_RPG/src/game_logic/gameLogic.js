import Player from './Player/Player';
import Enemy from './Enemies/Enemy';
import { attack, defend, activateItem } from './actions';

// The gameLogic object provides methods for handling the game's logic
const gameLogic = {
  // Initialize the player and enemy
  player: new Player('Player', 100, ['health potion']),
  enemy: new Enemy('Enemy', 100),

  // Function to handle the player's turn
  handleTurn(action) {
    if (action === 'attack') {
      attack(this.player, this.enemy);
    } else if (action === 'defend') {
      defend(this.player);
    } else if (action === 'use item') {
      activateItem(this.player);
    }
  },
};

export default gameLogic;