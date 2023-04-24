const form = document.querySelector('form');
const input = document.querySelector('input');
const chatBox = document.querySelector('#chat-box');

form.addEventListener('submit', async (event) => {
  event.preventDefault();

  // Get the user's message from the input field
  const message = input.value;

  // Clear the input field
  input.value = '';

  // Send the message to the server for processing
  const response = await fetch('/message', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ message })
  });

  // Display the server's response in the chat box
  const data = await response.json();
  const { reply } = data;

  const messageElement = document.createElement('div');
  messageElement.innerText = `User: ${message}`;
  chatBox.appendChild(messageElement);

  const replyElement = document.createElement('div');
  replyElement.innerText = `Bot: ${reply}`;
  chatBox.appendChild(replyElement);
});
