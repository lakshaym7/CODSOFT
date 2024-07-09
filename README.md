# CODSOFT

## Task 1 - CHATBOT WITH RULE-BASED RESPONSES
A basic implementation of a rule-based chatbot using Python. The chatbot can respond to a variety of user inputs with predefined responses. It uses a simple matching algorithm to determine the best response based on the user's message.

Features
  - Predefined Responses: The chatbot provides specific responses to common questions and phrases.
  - Keyword Matching: The chatbot uses keyword matching to determine the most appropriate response.
  - Fallback Response: If the chatbot cannot understand the user's input, it provides a generic fallback response.
  - Randomized Fallbacks: The fallback responses are randomized for a more dynamic interaction.

How It Works
  - Response Definitions: Predefined responses are stored in the longResponses.py file.
  - Message Processing: User messages are processed in main.py to determine the best response.  
  - Probability Calculation: The chatbot calculates the probability of each predefined response being the correct one based on the keywords present in the user's message.
  - Response Selection: The chatbot selects the response with the highest probability.
  - User Interaction: The chatbot interacts with the user in a loop, continuously taking user input and providing responses.


## Task 2 - TIC-TAC-TOE AI
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


## Task 3 - RECOMMENDATION SYSTEM
A simple movie recommendation system built using Python and machine learning techniques. The system uses a TF-IDF vectorizer to process movie overviews and calculates cosine similarity to recommend movies based on their content.

Features
  - Content-Based Filtering: Recommends movies based on the similarity of their overviews.
  - TF-IDF Vectorization: Converts movie overviews into numerical vectors using TF-IDF.
  - Cosine Similarity: Measures the similarity between movie vectors to find the most similar movies.
  - Top 10 Recommendations: Provides the top 10 most similar movies for a given input movie.

How It Works
  - Data Loading: The movie dataset is loaded from a CSV file.
  - Text Processing: Movie overviews are processed and converted into TF-IDF vectors.
  - Similarity Calculation: Cosine similarity is calculated between all movie vectors.
  - Recommendation: The system recommends the top 10 movies similar to the input movie based on cosine similarity.
