# Tic-Tac-Toe-Game

A simple command-line implementation of the classic Tic-Tac-Toe game using Python. This project allows two players to play the game in turns, with checks for winning conditions and the option to play until the board is full or a player wins.

## Introduction

Tic-Tac-Toe is a classic two-player game where players take turns marking spaces in a 3x3 grid. The player who succeeds in placing three of their marks in a horizontal, vertical, or diagonal row wins the game.

This project is designed to be a simple demonstration of fundamental programming concepts such as loops, conditionals, and basic data structures in Python.

## Features

- **Two-Player Game**: Supports two players taking turns.
- **Win Detection**: Detects winning conditions for both players horizontally, vertically, and diagonally.
- **Invalid Move Handling**: Ensures players cannot choose already occupied or invalid positions.
- **Game End Conditions**: Ends the game when a player wins or all positions are filled.

## Game Rules

1. **Players**: Two players, Player 01 and Player 02.
2. **Board**: A 3x3 grid where players place their marks ('X' for Player 01 and 'O' for Player 02).
3. **Turns**: Players take turns to place their marks in empty positions.
4. **Winning Conditions**: The first player to get three of their marks in a row, column, or diagonal wins the game.
5. **Draw**: If all nine positions are filled without a winner, the game is declared a draw.

## Technologies Used

- **Python**: The programming language used to implement the game logic.

## Setup

1. **Clone the Repository**:
   ```sh
   git clone https://github.com/Pudamya/Tic-Tac-Toe.git
   ```

2. **Navigate to the Repository Directory**:
   ```sh
   cd Tic-Tac-Toe
   ```

## Usage

1. **Run the Game**:
   ```sh
   python tic_tac_toe.py
   ```

2. **Gameplay**:
   - The game will display the board and prompt each player to choose a position.
   - Players input the position where they want to place their mark (e.g., P1, P2, P3, etc.).
   - The game checks for a win after each move and announces the winner or a draw.

## Contributing

Contributions are welcome! Please fork this repository and submit pull requests for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
