# CODSOFT

## Task 1 - Chatbot

## Task 2 - 
A Python implementation of the classic Tic-Tac-Toe game, featuring an AI opponent powered by the Minimax algorithm. The game is designed for two players: one human and one AI. The AI uses the Minimax algorithm to make optimal moves, ensuring a challenging and engaging gameplay experience.

Features
  - Human vs AI Gameplay: Play against a computer opponent that uses the Minimax algorithm to make decisions.
  - Dynamic Board Printing: The game board is printed dynamically after each move, allowing players to see the current state of the game.
  - Winner Detection: The game checks for a winner after each move and declares the winner if any.
  - Draw Detection: The game detects when the board is full and declares a draw if there is no winner.
  - Input Validation: The game validates the human player's input to ensure valid moves.
  
How It Works
  - Board Initialization: The game starts with an empty 3x3 board.
  - Player Moves: Players take turns to make their moves. The human player always plays as 'X', and the AI plays as 'O'.
  - Move Validation: The game checks if the move is valid (i.e., the chosen cell is empty).
  - Winner Detection: After each move, the game checks if there is a winner by evaluating rows, columns, and diagonals.
  - Minimax Algorithm: The AI uses the Minimax algorithm to evaluate possible moves and choose the optimal one. The algorithm recursively evaluates the game tree to find the move that          maximizes the AI's chances of winning or drawing.

Code Overview
  - create_board: Initializes an empty 3x3 board.
  - print_board: Prints the current state of the board.
  - is_move_valid: Checks if a move is valid.
  - make_move: Makes a move on the board.
  - isWinner: Checks if the specified player has won the game.
  - isGameover: Checks if the game is over (either a win or a draw).
  - miniMax: Implements the Minimax algorithm to evaluate moves.
  - findBestMove: Finds the best move for the AI using the Minimax algorithm.
  - playGame: The main function to start and play the game.

## Task 3 - 
