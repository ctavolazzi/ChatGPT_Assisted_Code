import React, { useState } from 'react';
import Game from './game';
import './App.css';

function App(Game) {
  // Initialize state variables
  const [currentChapter, setCurrentChapter] = useState('intro');
  const [player, setPlayer] = useState({
    name: 'Player',
    health: 100,
    inventory: ['health potion'],
  });

  // Function to handle the player's choice in the current chapter
  const handleChoice = choice => {
    // Update the current chapter based on the player's choice
    if (currentChapter === 'intro') {
      if (choice === 'forest') {
        setCurrentChapter('forest');
      } else if (choice === 'cave') {
        setCurrentChapter('cave');
      }
    } else if (currentChapter === 'forest') {
      if (choice === 'attack') {
        setPlayer({ ...player, health: player.health - 10 });
        setCurrentChapter('forest after attack');
      } else if (choice === 'defend') {
        setPlayer({ ...player, health: player.health - 5 });
        setCurrentChapter('forest after defend');
      } else if (choice === 'use item') {
        // Use a health potion from the player's inventory
        if (player.inventory.length > 0) {
          const item = player.inventory[0];
          if (item === 'health potion') {
            setPlayer({ ...player, health: player.health + 20 });
          }
          setPlayer({ ...player, inventory: player.inventory.slice(1) });
        }
        setCurrentChapter('forest after use item');
      }
    }
  };

  // Render the current chapter
  if (currentChapter === 'intro') {
    return (
      <div>
        <p>You find yourself in a dark forest. There is a path leading into the forest and a cave nearby.</p>
        <p>
          What do you do?
          <button onClick={() => handleChoice('forest')}>Enter the forest</button>
          <button onClick={() => handleChoice('cave')}>Explore the cave</button>
        </p>
      </div>
    );
  } else if (currentChapter === 'forest') {
    return (
      <div>
        <p>You continue down the path and encounter a fierce enemy!</p>
        <p>
          What do you do?
          <button onClick={() => handleChoice('attack')}>Attack the enemy</button>
          <button onClick={() => handleChoice('defend')}>Defend against the enemy's attack</button>
          <button onClick={() => handleChoice('use item')}>Use an item from your inventory</button>
        </p>
      </div>
    );
  } else if (currentChapter === 'forest after attack') {
    return (
      <div>
        <p>You attack the enemy and deal 10 points of damage.</p>
        <p>The enemy counterattacks and deals 10 points of damage to you.</p>
        <p>
          Your current health: {player.health}
        <br />
          What do you do next?
          <button onClick={() => handleChoice('attack')}>Attack the enemy again</button>
          <button onClick={() => handleChoice('defend')}>Defend against the enemy's next attack</button>
          <button onClick={() => handleChoice('use item')}>Use an item from your inventory</button>
        </p>
      </div>
);
} else if (currentChapter === 'forest after defend') {
return (
<div>
<p>You defend against the enemy's attack and take 5 points of damage instead of 10.</p>
<p>
Your current health: {player.health}
<br />
What do you do next?
<button onClick={() => handleChoice('attack')}>Attack the enemy</button>
<button onClick={() => handleChoice('defend')}>Defend against the enemy's next attack</button>
<button onClick={() => handleChoice('use item')}>Use an item from your inventory</button>
</p>
</div>
);
} else if (currentChapter === 'forest after use item') {
return (
<div>
<p>You use a health potion and regain 20 points of health.</p>
<p>
Your current health: {player.health}
<br />
What do you do next?
<button onClick={() => handleChoice('attack')}>Attack the enemy</button>
<button onClick={() => handleChoice('defend')}>Defend against the enemy's next attack</button>
<button onClick={() => handleChoice('use item')}>Use an item from your inventory</button>
</p>
</div>
);
} else if (currentChapter === 'cave') {
return (
<div>
<p>You explore the cave and find a treasure
chest! Inside, you find a magical sword that increases your attack power.</p>

<p>
Your inventory: {player.inventory.join(', ')}
<br />
What do you do next?
<button onClick={() => handleChoice('forest')}>Return to the forest</button>
<button onClick={() => handleChoice('cave')}>Explore the cave further</button>
</p>
</div>
);
} else {
return (
<div>
<p>The adventure continues...</p>
</div>
);
}
}
export default App;