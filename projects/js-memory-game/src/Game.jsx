import { useState, useMemo, useEffect } from "react";
import "../src/App.css";
import GridButton from "./Components/GridButton";

function splitArray(array) {
  let arr = [];
  for (let i = 0; i < array.length; i += 4) {
    arr.push(array.slice(i, i + 4));
  }
  return arr;
}

function shuffleArray(array) {
  for (let i = array.length - 1; i > 0; i--) {
    var j = Math.floor(Math.random() * (i + 1));
    var temp = array[i];
    array[i] = array[j];
    array[j] = temp;
  }
  return array;
}
function getRandomNumber(n = 8) {
  const r = n / 2;
  const arr_numbers = [];
  for (let index = 0; index < r; index++) {
    for (let j = 0; j < 2; j++) {
      arr_numbers.push(index);
    }
  }
  return shuffleArray(arr_numbers);
}

function Game() {
  const [gridMatrix, setGridMatrix] = useState(8);
  const [grid, setGrid] = useState([]);
  const [blocksActive, setBlocksActive] = useState([]);
  const [score, setScore] = useState(0);
  const [numTries, setNumTries] = useState(0);
  const [state, setState] = useState("Dialog");

  useEffect(() => {
    ScrollLock();
  }, [state]);

  function handleRangeChange(e) {
    const data = e.target.value;
    setGridMatrix(data);
    console.log(gridMatrix);
  }

  const initGrid = useMemo(() => {
    const randomNumbers = getRandomNumber(gridMatrix);
    const arr = Array.from({ length: gridMatrix }).map((_, index) => {
      return {
        index: index,
        isActive: false,
        value: randomNumbers[index],
        status: false,
      };
    });
    setGrid(arr);
    return arr;
  }, [gridMatrix]);

  function ScrollLock() {
    if (state === "Playing") {
      document.querySelector("body").style.overflow = "";
    } else if (state === "Dialog") {
      document.querySelector("body").style.overflow = "hidden";
    }
  }

  function checkActiveBlocks(blocksActive) {
    const b1 = grid[blocksActive[0]];
    const b2 = grid[blocksActive[1]];
    const g = grid;

    if (blocksActive.length == 2) {
      if (grid[blocksActive[0]].value === grid[blocksActive[1]].value) {
        setTimeout(() => {
          setScore((prev) => prev + 1);
          b1.status = "success";
          b2.status = "success";
          g[blocksActive[0]] = b1;
          g[blocksActive[1]] = b2;
          setGrid([...g]);
          setBlocksActive([]);
        }, 1000);
      } else {
        setTimeout(() => {
          b1.status = "error";
          b2.status = "error";
          g[blocksActive[0]] = b1;
          g[blocksActive[1]] = b2;
          setGrid([...g]);
        }, 1000);

        setTimeout(() => {
          setNumTries((prev) => prev + 1);
          b1.isActive = false;
          b2.isActive = false;
          b1.status = "";
          b2.status = "";
          g[blocksActive[0]] = b1;
          g[blocksActive[1]] = b2;

          setGrid([...g]);
          setBlocksActive([]);
        }, 1500);
      }
    }
  }

  function showValue(id) {
    if (blocksActive.length < 2) {
      const block = grid.find((c) => c.index == id);
      if (block.isActive == false) {
        block.isActive = true;
        const g = grid;

        g[block.index] = block;
        const a = [...blocksActive, block.index];
        setBlocksActive(a);
        checkActiveBlocks(a);
        setGrid([...g]);

        if (g.every((b) => b.isActive == true)) {
          setTimeout(() => {
            setState("Over");
          }, 1000);
        }
      }
    }
  }

  function resetGame() {
    setState("Dialog");
    setNumTries(0);
    setScore(0);
    setBlocksActive([]);
    setGrid(initGrid);
  }
  const grid_chunk = splitArray(grid);
  return (
    <>
      {state === "Dialog" && (
        <>
          <div className="dialog__overlay">
            <div className="dialog">
              <p>Enter your grid dimensions:</p>
              <div className="dialog__range">
                <span>{gridMatrix}</span>
                <input
                  type="range"
                  min={4}
                  max={32}
                  step={4}
                  defaultValue={gridMatrix}
                  onChange={(e) => {
                    handleRangeChange(e);
                  }}
                />
                <span>{32}</span>
              </div>
              <button
                onClick={() => {
                  setState("Playing");
                }}
              >
                Play!
              </button>
            </div>
          </div>
        </>
      )}
      <div className="container">
        {state === "Dialog" && <div className="overlay"></div>}
        <div className="intro">
          <h1>Memory Game</h1>
          {state == "Over" && <h1 style={{ color: "green" }}>You win!</h1>}

          <div className="stats">
            <p>Number of tries: {numTries}</p>
            <p>Total Score: {score}</p>
          </div>
        </div>
        <ul className="grid">
          {grid.length == 0 ? (
            <>Something happened.</>
          ) : (
            <>
              {grid_chunk.map((c, i) => (
                <li
                  key={i}
                  className={`grid__row ${
                    i == grid_chunk.length - 1 ? "bottom_level" : ""
                  } ${i == 0 ? "top_level" : ""}`}
                >
                  {c.map((g, idx) => (
                    <GridButton key={idx} data={g} showValue={showValue} />
                  ))}
                </li>
              ))}
            </>
          )}
        </ul>
        {state == "Over" && (
          <button onClick={resetGame} className="retry">
            Retry
          </button>
        )}
      </div>
    </>
  );
}

export default Game;
