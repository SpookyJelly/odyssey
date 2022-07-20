import { useState, useRef } from "react";
import reactLogo from "./assets/react.svg";
import "./App.scss";
import axios from "axios";
import { config } from "./config/config";

function App() {
  const [joke, setJoke] = useState<string>("Odyssey");
  const ref = useRef<HTMLImageElement>(null);

  const getSimpleJoke = async () => {
    try {
      if (ref.current) ref.current.className = "logo";
      const URL = config.serverUrl;
      const res = await axios.get(`${URL}/api/random`);
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
      <header>
        <button>test</button>
        <div>
          <p>asdasd</p>
        </div>
      </header>
      <section>
        <div>
          <img ref={ref} src={reactLogo} />
          <div>
            <p className="typo">{joke}</p>
          </div>
        </div>
        <button onClick={getSimpleJoke}>Get Daily Joke</button>
      </section>
      <footer></footer>
    </div>
  );
}

export default App;
