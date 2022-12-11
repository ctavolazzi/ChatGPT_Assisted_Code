import React from 'react';
import logo from './logo.svg';
import './App.css';
import gameLogic from './game_logic/gameLogic';

class App extends React.Component {
  // Initialize state variables
  state = {
    playerHealth: 100,
    enemyHealth: 100,
    playerInventory: ['health potion'],
  }

  // Function to handle the player's turn
  handleTurn = (action) => {
    gameLogic.handleTurn(action, this.state, this.setState);

    // Enemy's turn
    // Attack the player, reducing their health
    this.setState({ playerHealth: this.state.playerHealth - 10 });
  }

  render() {
    const { playerHealth, enemyHealth, playerInventory } = this.state;

    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />

          {/* Display the player's health */}
          <p>Player health: {playerHealth}</p>

          {/* Display the enemy's health */}
          <p>Enemy health: {enemyHealth}</p>

          {/* Display the player's inventory */}
          <p>Inventory: {playerInventory.join(', ')}</p>

          {/* Allow the player to choose an action */}
          <p>
            Choose an action:
            <button onClick={() => this.handleTurn('attack')}>Attack</button>
            <button onClick={() => this.handleTurn('defend')}>Defend</button>
            <button onClick={() => this.handleTurn('use item')}>Use Item</button>
          </p>
        </header>
      </div>
    );
  }
}

export default App;
