import { useState, useRef, FormEvent } from "react";
import reactLogo from "./assets/react.svg";
import "./App.scss";
import { getRandomJoke, translateJoke } from "./services/request";
import { findProperJokefromResponse } from "./utils/finder";
import { JokeResponse } from "./models/VO";
import { validateHuman } from "./utils/validator";

//TODO: define error handler
function App() {
  //NOTE: 변경, 추가 등 다방면으로 활용할 여지가 있어 상태로 관리
  const [jokeResponse, setJokeResponse] = useState<JokeResponse>();
  const [inputVisiable, setInputVisiable] = useState<boolean>(false);
  // const [joke, setJoke] = useState<string>("Odyssey");
  const [joke, setJoke] = useState<{ id: string; value: string }>({
    id: "init",
    value: "Odyssey",
  });
  const ref = useRef<HTMLImageElement>(null);

  const getSimpleJoke = async () => {
    try {
      if (ref.current) ref.current.className = "logo";

      const response = await getRandomJoke();
      const jokeObj = findProperJokefromResponse(response);
      //NOTE: check timing of jokeresponse
      setJokeResponse(response);
      // korJoke는 id가 number이므로 변환.
      setJoke({ id: String(jokeObj.id), value: jokeObj.value });
      setInputVisiable(jokeObj.lang === "ENG" ? true : false);
    } catch (e) {
      console.log("e", e);
    } finally {
      if (ref.current) ref.current.className = "";
    }
  };

  const stateToActive = (state: boolean) => {
    return state ? "active" : "";
  };
  const handleSubmit = async (e: FormEvent) => {
    e.preventDefault();
    // console.log(e.target);
    const data = new FormData(e.target as HTMLFormElement);
    // console.log("joke Obj", jokeResponse);
    const validateResult = await validateHuman();
    if (validateResult) {
      try {
        translateJoke(joke.id, data);
      } catch (e) {
        console.log("e", e);
      } finally {
        setInputVisiable(false);
      }
    }
    setInputVisiable(false);
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
            <span>✅</span>
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
          <li>
            스테이징 단계 추가 <span>❌</span>
          </li>
          <li>
            리캡챠 추가 <span>❌</span>
          </li>
        </div>
      </header>
      <section>
        <div>
          <img ref={ref} src={reactLogo} />
          <div>
            <p className="typo">{joke.value}</p>
          </div>
          <div id="holder" style={{ position: "relative" }}>
            <div className={`input-wrapper ${stateToActive(inputVisiable)}`}>
              <form action="" onSubmit={handleSubmit} name="submitForm">
                <p>Lorem ipsum dolor sit.</p>
                <textarea
                  placeholder="재미있는 번역 부탁드리겠습니다."
                  name="value"
                />
                <div className="submit-btn-container">
                  <div className="dummy"></div>
                  <div className="content">
                    <button className="submit-btn" type="submit">
                      Submit
                    </button>
                  </div>
                </div>
              </form>
            </div>
            <button
              onClick={getSimpleJoke}
              className={`joke-btn ${stateToActive(inputVisiable)}`}
            >
              Get Daily Joke
            </button>
          </div>
        </div>
      </section>
      <footer>
        <span>Spookyjelly</span>
      </footer>
    </div>
  );
}

export default App;
