from typing import List, Tuple, Optional

def create_board() -> List[List[str]]:
    return [[" " for _ in range(3)] for _ in range(3)]

def print_board(board: List[List[str]]) -> None:
    for row in board:
        print("|".join(row))
        print("------")

def is_move_valid(board: List[List[str]], row: int, col: int) -> bool:
    return board[row][col] == ' '

def make_move(board: List[List[str]], row: int, col: int, player: str) -> None:
    board[row][col] = player

def isWinner(board: List[List[str]], player: str) -> bool:
    for i in range(3):
        if all([cell == player for cell in board[i]]) or all([board[j][i] == player for j in range(3)]):
            return True
    if (board[0][0] == board[1][1] == board[2][2] == player) or (board[0][2] == board[1][1] == board[2][0] == player):
        return True
    return False

def isGameover(board: List[List[str]]) -> bool:
    return isWinner(board, player='X') or isWinner(board, player='O') or all(" " not in row for row in board)

def miniMax(board: List[List[str]], depth: int, maximizing_player: bool) -> int:
    if isWinner(board, "X"):
        return -1
    if isWinner(board, "O"):
        return 1
    if isGameover(board):
        return 0
    
    if maximizing_player:
        best_Score = float('-inf')
        for row in range(3):
            for col in range(3):
                if is_move_valid(board, row, col):
                    board[row][col] = 'O'
                    score = miniMax(board, depth + 1, False)
                    board[row][col] = " "
                    best_Score = max(score, best_Score)
        return best_Score
    else:
        best_Score = float('inf')
        for row in range(3):
            for col in range(3):
                if is_move_valid(board, row, col):
                    board[row][col] = 'X'
                    score = miniMax(board, depth + 1, True)
                    board[row][col] = " "
                    best_Score = min(score, best_Score)
        return best_Score
    
def findBestMove(board: List[List[str]]) -> Tuple[int, int]:
    best_Score = float('-inf')
    best_move = None
    for row in range(3):
        for col in range(3):
            if is_move_valid(board, row, col):
                board[row][col] = 'O'
                score = miniMax(board, 0, False)
                board[row][col] = " "
                if score > best_Score:
                    best_Score = score
                    best_move = (row, col)
    return best_move

def playGame() -> None:
    board = create_board()
    current_player = "X"
    print_board(board)
    while not isGameover(board):
        if current_player == 'X':
            while True:
                try:
                    row, col = map(int, input('Enter the row and column (0, 1, or 2) separated by space: ').split())
                    if row not in range(3) or col not in range(3):
                        print("Invalid input. Please enter numbers 0, 1, or 2.")
                        continue
                    break
                except ValueError:
                    print("Invalid input. Please enter two integers separated by space.")
        else:
            row, col = findBestMove(board)
            print(f"AI's move is {row}, {col}") 
        
        if is_move_valid(board, row, col):
            make_move(board, row, col, current_player)
            print_board(board)
            print("\n")
            if isWinner(board, current_player):
                print(f"{current_player} wins\n")
                break 
            current_player = "O" if current_player == "X" else "X"
        else:
            print("Invalid move. Try again.")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    playGame()
