import React, { useState } from "react";
import axios from "axios";
import { TextField, Button, List, ListItem } from "@mui/material";

const Chatbot = () => {
  const [query, setQuery] = useState("");
  const [history, setHistory] = useState([]);
  const [response, setResponse] = useState("");

  const handleQuery = async () => {
    try {
      const res = await axios.get("http://localhost:8000/api/chatbot/", {
        params: { query },
      });
      setHistory([...history, { query, response: res.data.summary }]);
      setResponse(res.data.summary);
      setQuery("");
    } catch (error) {
      console.error(error);
      setResponse("Error processing query.");
    }
  };

  return (
    <div style={{ padding: "1rem", maxWidth: "600px", margin: "auto" }}>
      <TextField
        fullWidth
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        label="Enter your query"
      />
      <Button
        variant="contained"
        color="primary"
        onClick={handleQuery}
        style={{ marginTop: "1rem" }}
      >
        Submit
      </Button>
      <div style={{ marginTop: "2rem" }}>
        <h3>Response:</h3>
        <p>{response}</p>
      </div>
      <div style={{ marginTop: "2rem" }}>
        <h3>Query History:</h3>
        <List>
          {history.map((item, index) => (
            <ListItem key={index}>
              <strong>Query:</strong> {item.query} <br />
              <strong>Response:</strong> {item.response}
            </ListItem>
          ))}
        </List>
      </div>
    </div>
  );
};

export default Chatbot;
