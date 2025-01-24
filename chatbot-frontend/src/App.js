import React, { useState } from 'react';
import './App.css';

function App() {
  const [userInput, setUserInput] = useState('');
  const [response, setResponse] = useState('');
  const [loading, setLoading] = useState(false);
  const [chatHistory, setChatHistory] = useState([]);

  const handleInputChange = (event) => {
    setUserInput(event.target.value);
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    if (!userInput) return;

    setLoading(true);

    // Update chat history with user message
    setChatHistory([...chatHistory, { sender: 'user', message: userInput }]);
    setUserInput(''); // Clear input field

    try {
      const response = await fetch('http://localhost:8000/chatbot/respond/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ message: userInput }), // Send user input to backend
      });

      const data = await response.json();

      if (data.response) {
        setChatHistory((prevChatHistory) => [
          ...prevChatHistory,
          { sender: 'bot', message: data.response }, // Add bot response to history
        ]);
      } else {
        setChatHistory((prevChatHistory) => [
          ...prevChatHistory,
          { sender: 'bot', message: 'Error: ' + data.error },
        ]);
      }
    } catch (error) {
      setChatHistory((prevChatHistory) => [
        ...prevChatHistory,
        { sender: 'bot', message: 'Error communicating with the backend.' },
      ]);
      console.error(error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="App">
      <div className="chat-container">
        <h1 className="title">AI Chatbot</h1>

        <div className="chat-box">
          {/* Display chat history */}
          {chatHistory.map((chat, index) => (
            <div
              key={index}
              className={chat.sender === 'user' ? 'user-message' : 'bot-message'}
            >
              <p>{chat.message}</p>
            </div>
          ))}

          {/* Display loading indicator */}
          {loading && <div className="loading">Thinking...</div>}
        </div>

        <form className="input-form" onSubmit={handleSubmit}>
          <input
            type="text"
            className="input-field"
            value={userInput}
            onChange={handleInputChange}
            placeholder="Ask me anything about products!"
          />
          <button type="submit" className="send-button">Send</button>
        </form>
      </div>
    </div>
  );
}

export default App;
