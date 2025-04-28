

import math

# Tic-Tac-Toe Board Representation
AI = 'X'   # AI plays as 'X'
HUMAN = 'O'  # Opponent plays as 'O'
EMPTY = ' '  # Empty spot

# Function to check if the game is over
def check_winner(board):
    winning_combinations = [(0,1,2), (3,4,5), (6,7,8),  # Rows
                            (0,3,6), (1,4,7), (2,5,8),  # Columns
                            (0,4,8), (2,4,6)]           # Diagonals

    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != EMPTY:
            return board[combo[0]]  # Return 'X' or 'O' as winner

    if EMPTY not in board:
        return "DRAW"  # If no moves left, it's a draw

    return None  # Game not over

# Function to evaluate the board
def evaluate(board):
    winner = check_winner(board)
    if winner == AI:
        return 10
    elif winner == HUMAN:
        return -10
    return 0  # Draw

# Minimax Algorithm Implementation
def minimax(board, depth, is_maximizing):
    score = evaluate(board)

    # Base cases: If game is over, return the score
    if score == 10 or score == -10:
        return score
    if EMPTY not in board:
        return 0  # Draw

    if is_maximizing:
        best = -math.inf
        for i in range(9):
            if board[i] == EMPTY:
                board[i] = AI
                best = max(best, minimax(board, depth + 1, False))
                board[i] = EMPTY  # Undo move
        return best
    else:
        best = math.inf
        for i in range(9):
            if board[i] == EMPTY:
                board[i] = HUMAN
                best = min(best, minimax(board, depth + 1, True))
                board[i] = EMPTY  # Undo move
        return best

# Find the best move for AI
def find_best_move(board):
    best_value = -math.inf
    best_move = -1

    for i in range(9):
        if board[i] == EMPTY:
            board[i] = AI
            move_value = minimax(board, 0, False)
            board[i] = EMPTY  # Undo move

            if move_value > best_value:
                best_value = move_value
                best_move = i

    return best_move

# Example Tic-Tac-Toe board
board = ['', 'O', 'X',
         ' ', 'O', 'O ',
         ' ', ' X', 'X']

best_move = find_best_move(board)
print(f"AI should play at position: {best_move}")

