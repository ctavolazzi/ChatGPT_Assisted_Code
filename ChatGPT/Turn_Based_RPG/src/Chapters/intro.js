import React from 'react';

// The Intro component displays the game introduction and provides
// a button for the player to start the game
const Intro = ({ onStart }) => (
  <div>
    <p>Welcome to the turn-based RPG!</p>
    <p>In this game, you will face off against an enemy in a series of turns.</p>
    <p>On each turn, you can choose to attack, defend, or use an item from your inventory.</p>
    <p>Are you ready to begin?</p>
    <button onClick={onStart}>Start Game</button>
  </div>
);

export default Intro;
