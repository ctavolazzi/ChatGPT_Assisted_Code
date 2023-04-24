// Desc: Main app component
import './App.css';
import { useState } from 'react';

function App() {

  // get the models from the api
  // useEffect(() => {
  //   getEngines();
  // }, [])

// add state for input and chat log
  const [input, setInput] = useState("");
  // const [models, setModels] = useState([]);
  const [chatLog, setChatLog] = useState([
    {user: "gpt", message: "Hello, I am GPT-3. How can I help you today?"},
  ]);

  // clear the chat log
  function clearChat() {
    setChatLog([]);
  }

  // function getEngines() {
  //   fetch("http://localhost:3080/models") // fetch the models from the api
  //     .then((response) => response.json())
  //     .then((data) => {
  //       setModels(data.models.data)
  //     }
  //   )
  // }

  // add a function to handle the form submit
  async function handleSubmit(e) {
    e.preventDefault();
    console.log('input: ', input);
    let chatLogNew = [...chatLog, {user: "me", message: `${input}`}];
    setChatLog(chatLogNew);

    console.log('chatLog: ', chatLog);
    for (let i = 0; i < chatLog.length; i++) {
      console.log('chatLog[i]: ', chatLog[i]);
    }
    const messages = chatLogNew.map((message) => message.message).join("\n");
    setInput("");

    // fetch response to the api combining the chat log array of messages and sending it as a message to localhost:3080 as a post
    const response = await fetch("http://localhost:3080", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        message: messages
      })
    });

    // get the response from the api and add it to the chat log
    const data = await response.json();
    setChatLog([...chatLogNew, {user: "gpt", message: `${data.message}`}]);
    console.log('chatLog: ', chatLog);
  }

  return (
    <div className="App">
      <aside className="sidemenu">
        <div className="side-menu-button" onClick={clearChat}>
          <span>+</span>
          New Chat
        </div>
        {/* <div className="models">
          <select>
            {models.map((model, index) => {
              return <option key={model.id} value={model.id}>{model.id}</option>
            })}
          </select>
        </div> */}
      </aside>
      <section className="chatbox">
        <div className="chat-log">
          {chatLog.map((message, index) => {
            return <ChatMessage key={index} message={message}/>
          })}
        </div>

        <div className="chat-input-holder">
          <form onSubmit={handleSubmit} className="chat-input-form">
            <input
              rows="1"
              value={input}
              onChange={(e) => setInput(e.target.value)}
              className="chat-input-textarea"></input>
            {/* <button className="chat-input-button">
              <span>Send</span>
            </button> */}
          </form>
        </div>
      </section>
    </div>
  );
}

const ChatMessage = ({message}) => {
  return (
    <div className={`chat-message ${message.user === "gpt" && "chatgpt"}`}>
      <div className="chat-message-center">
        <div className={`avatar ${message.user === "gpt" && "chatgpt"}`}>
          {/* {message.user === "gpt" ? "G" : "M"} */}
        </div>
        <div className="message">
          {message.message}
        </div>
      </div>
    </div>
  )
}

export default App;
