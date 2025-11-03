import React, { useState } from "react";
import Board from "./Board";
import "./App.css";

function App() {
  const [board, setBoard] = useState(Array(9).fill(null));
  const [xIsNext, setXIsNext] = useState(true);
  const [winner, setWinner] = useState(null);

  // Helper: determine winner
  const calculateWinner = (squares) => {
    const lines = [
      [0, 1, 2],
      [3, 4, 5],
      [6, 7, 8],
      [0, 3, 6],
      [1, 4, 7],
      [2, 5, 8],
      [0, 4, 8],
      [2, 4, 6],
    ];
    for (let [a, b, c] of lines) {
      if (squares[a] && squares[a] === squares[b] && squares[a] === squares[c]) {
        return squares[a];
      }
    }
    return null;
  };

  // Handle click on a square
  const handleClick = (i) => {
    if (board[i] || winner) return; // ignore if occupied or game over
    const newBoard = board.slice();
    newBoard[i] = xIsNext ? "X" : "O";
    setBoard(newBoard);
    const gameWinner = calculateWinner(newBoard);
    if (gameWinner) {
      setWinner(gameWinner);
    } else if (!newBoard.includes(null)) {
      setWinner("Draw");
    }
    setXIsNext(!xIsNext);
  };

  // Reset the game
  const resetGame = () => {
    setBoard(Array(9).fill(null));
    setXIsNext(true);
    setWinner(null);
  };

  const status = winner
    ? winner === "Draw"
      ? "It's a draw!"
      : `🎉 Player ${winner} wins!`
    : `Current Player: ${xIsNext ? "X" : "O"}`;

  return (
    <div className="app">
      <h1>🎮 Tic Tac Toe</h1>
      <p>{status}</p>
      <Board squares={board} onClick={handleClick} />
      <button className="reset" onClick={resetGame}>
        🔄 Restart Game
      </button>
    </div>
  );
}

export default App;