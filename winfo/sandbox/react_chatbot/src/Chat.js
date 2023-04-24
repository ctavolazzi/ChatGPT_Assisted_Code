import React, { useState, useEffect } from 'react';
import axios from 'axios';

function Chat() {
  const [prompt, setPrompt] = useState('');
  const [messages, setMessages] = useState([]);

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (prompt === '') {
      return;
    }

    setMessages((messages) => [...messages, { type: 'user', message: prompt }]);
    setPrompt('');

    try {
      const response = await axios.post('/api/openai', { message: prompt });
      const message = response.data.data;

      setMessages((messages) => [...messages, { type: 'bot', message }]);
      scrollToBottom();
    } catch (error) {
      console.error(error);
    }
  };

  const scrollToBottom = () => {
    const chatBox = document.getElementById('chat-box');
    chatBox.scrollTop = chatBox.scrollHeight;
  };

  return (
    <div className="chat-container">
      <div id="chat-box" className="chat-box">
        {messages.map((message, index) => (
          <div key={index} className={`message ${message.type}`}>
            {message.message}
          </div>
        ))}
      </div>
      <form onSubmit={handleSubmit} className="input-form">
        <input
          type="text"
          placeholder="Type your message here..."
          value={prompt}
          onChange={(e) => setPrompt(e.target.value)}
          className="input-field"
        />
        <button type="submit" className="send-button">
          Send
        </button>
      </form>
    </div>
  );
}

export default Chat;
