import { useState, useRef } from "react";
import reactLogo from "./assets/react.svg";
import "./App.css";
import axios from "axios";

function App() {
  const [joke, setJoke] = useState<string>("Odyssey");
  const ref = useRef<HTMLImageElement>(null);

  const getSimpleJoke = async () => {
    try {
      if (ref.current) ref.current.className = "logo";
      const res = await axios.get("http://localhost:8000");
      const joke = res.data.ENG.value;
      setJoke(joke);
    } catch (e) {
      console.log("e", e);
    } finally {
      if (ref.current) ref.current.className = "";
    }
  };

  return (
    <div className="App">
      <div>
        <img ref={ref} src={reactLogo} />
        <p>{joke}</p>
      </div>
      <button onClick={getSimpleJoke}>Get Daily Joke</button>
    </div>
  );
}

export default App;
