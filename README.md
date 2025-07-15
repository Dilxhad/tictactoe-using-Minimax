# tictactoe-using-Minimax

## Tic Tac Toe with Minimax AI

This is a Python implementation of the classic Tic Tac Toe game, featuring an unbeatable AI using the **Minimax algorithm**.

The project was part of the [CS50's Introduction to Artificial Intelligence with Python](https://cs50.harvard.edu/ai/) course.

---

## 🎮 How It Works

- The game uses **Pygame** for a graphical interface.
- You can choose to play as `X` or `O`.
- The computer uses the **Minimax algorithm** to play optimally.
- The game ends when there's a winner or a tie.

---

## 📁 Files

- `runner.py`: Handles the graphical interface using Pygame.  
  > ⚠️ *This file was provided as part of the CS50 assignment and was not written by me.*

- `tictactoe.py`: Contains all the core logic of the game, including:
  - Game state handling
  - Move generation
  - Win/tie detection
  - Minimax algorithm for the AI player  
  > ✅ *This file was fully implemented by me.*

---

## 🚀 How to Run

1. Make sure you have Python and Pygame installed:
   ```bash
   pip install pygame
