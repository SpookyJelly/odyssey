import { useState, useRef } from "react";
import reactLogo from "./assets/react.svg";
import "./App.scss";
import { getRandomJoke } from "./services/request";
import { findProperJokefromResponse } from "./utils/finder";
import { JokeResponse } from "./models/VO";

function App() {
  //NOTE: 변경, 추가 등 다방면으로 활용할 여지가 있어 상태로 관리
  const [jokeResponse, setJokeResponse] = useState<JokeResponse>();
  const [inputVisiable, setInputVisiable] = useState<boolean>(false);
  const [joke, setJoke] = useState<string>("Odyssey");
  const ref = useRef<HTMLImageElement>(null);

  const getSimpleJoke = async () => {
    try {
      if (ref.current) ref.current.className = "logo";

      const response = await getRandomJoke();
      const jokeObj = findProperJokefromResponse(response);
      //NOTE: check timing of jokeresponse
      setJokeResponse(response);
      setJoke(jokeObj.value);
      setInputVisiable(jokeObj.lang === "ENG" ? true : false);
    } catch (e) {
      console.log("e", e);
    } finally {
      if (ref.current) ref.current.className = "";
    }
  };
  const tester = (state: boolean) => {
    return state ? "block" : "none";
  };
  const testing = (state: boolean) => {
    return state ? "active" : "";
  };

  return (
    <div className="App">
      <header>
        <div className="todo-btn-wrapper">
          <button style={{ cursor: "default" }}>TODOS</button>
        </div>
        <div className="todo-card">
          <li>
            유저 번역 기능 추가
            <span>❌</span>
          </li>
          <li>
            타이포 애니메이션 추가 <span>❌</span>
          </li>
          <li>
            배경 및 캐릭터 스프라이트 추가 <span>❌</span>
          </li>
          <li>
            투표 기능 추가 <span>❌</span>
          </li>
        </div>
      </header>
      <section>
        <div>
          <img ref={ref} src={reactLogo} />
          <div>
            <p className="typo">{joke}</p>
          </div>
          <div id="holder" style={{ position: "relative" }}>
            <div className={`input-wrapper ${testing(inputVisiable)}`}>
              <p>Lorem ipsum dolor sit.</p>
              <input />
            </div>
            <button
              onClick={getSimpleJoke}
              className={`btn ${testing(inputVisiable)}`}
            >
              Get Daily Joke
            </button>
          </div>
        </div>
      </section>
      <footer></footer>
    </div>
  );
}

export default App;
