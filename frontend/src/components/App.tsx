import React, { useState } from "react";

import AxiosClient from "../api/axiosClient";

function App() {
  const [textInput, setTextInput] = useState("");
  const [output, setOutput] = useState("");

  const handleSubmit = () => {
    AxiosClient.get(`/api/test?text=${textInput}`)
      .then((res) => {
        setOutput(res.data.text);
      })
      .catch((err) => console.log(err));
  };

  return (
    <div>
      <h1 className="font-bold underline">Hello world!</h1>
      <header>
        <pre>django-react-heroku-template</pre>
        <p>
          Edit <code>src/App.tsx</code> and save to reload.
        </p>

        <div>
          <p>Test connection with API:</p>
          <label htmlFor="char-input">Make this text uppercase: </label>
          <input
            id="char-input"
            type="text"
            value={textInput}
            onChange={(e) => setTextInput(e.target.value)}
          />
          <button onClick={handleSubmit}>Submit</button>
          <h3>{output}</h3>
        </div>
      </header>
    </div>
  );
}

export default App;
