import math

def check_winner(board, player):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if all([board[i][j] == player for j in range(3)]) or all([board[j][i] == player for j in range(3)]):
            return True
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    return False

def is_board_full(board):
    # Check if all spaces on the board are filled
    return all(board[i][j] != 0 for i in range(3) for j in range(3))

def min_max(board, depth, is_maximizing):
    # If AI wins, return a large positive value
    if check_winner(board, 1): return 10 - depth  
    # If opponent wins, return a large negative value
    if check_winner(board, -1): return depth - 10 
    # If the board is full and no one won, return 0 (draw)
    if is_board_full(board): return 0  
    
    if is_maximizing:
        best = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == 0:
                    board[i][j] = 1  # AI move
                    best = max(best, min_max(board, depth + 1, False))
                    board[i][j] = 0  # Undo move
        return best
    else:
        best = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == 0:
                    board[i][j] = -1  # Opponent move
                    best = min(best, min_max(board, depth + 1, True))
                    board[i][j] = 0  # Undo move
        return best
    
def find_best_move(board):
    best_val = -math.inf
    best_move = (-1, -1)
    
    # Try every possible move for the AI and evaluate it using minimax
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:  # Empty spot
                board[i][j] = 1  # AI move
                move_val = min_max(board, 0, False)
                board[i][j] = 0  # Undo move
                
                # Choose the best move with the highest minimax value
                if move_val > best_val:
                    best_val = move_val
                    best_move = (i, j)
    return best_move

# Test board (1 = AI, -1 = opponent, 0 = empty)
board = [
    [1, -1, 1],
    [0, -1, 0],
    [1, 0, 0]
]

best_move = find_best_move(board)
print(f"Best move for AI: Row {best_move[0]}, Column {best_move[1]}")
