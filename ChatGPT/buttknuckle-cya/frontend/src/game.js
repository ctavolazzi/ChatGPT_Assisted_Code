import React, { useState } from "react";

const Game = (props) => {
  const [story, setStory] = useState("");
  const [decision, setDecision] = useState("");

  const handleDecision = (event) => {
    setDecision(event.target.value);
  };

  const handleSubmit = () => {
    // Send decision to Node server
    fetch("http://localhost:3000/game", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ decision }),
    })
      .then((res) => res.json())
      .then((data) => {
        setStory(data.story);
      });
  };

  return (
    <div>
      <p>{story}</p>
      <form onSubmit={handleSubmit}>
        <label>
          <input type="radio" value="option1" onChange={handleDecision} />
          Option 1
        </label>
        <label>
          <input type="radio" value="option2" onChange={handleDecision} />
          Option 2
        </label>
        <input type="submit" value="Submit" />
      </form>
    </div>
  );
};

export default Game;
