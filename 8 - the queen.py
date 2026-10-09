8 - the queen
def is_safe (board, row, col):
    for i in range (row):
        if board [i][col] == 'Q':
            return False
            
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board [i][j] == 'Q':
            return False
            
        i -= 1
        j -= 1
        
    i, j = row - 1, col + 1
    while i >= 0 and j < 8:
        if board [i][j] == 'Q':
            return False
            
        i -= 1
        j += 1
        
    return True
def is_safe(board, row, col):
    # Check this column for another queen
    for i in range(row):
        if board[i][col] == 'Q':
            return False
            
    # Check upper-left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False
            
    # Check upper-right diagonal
    for i, j in zip(range(row, -1, -1), range(col, 8)):
        if board[i][j] == 'Q':
            return False
            
    return True

def solve_8queens(board, row):
    # Base case: If all queens are placed, return True
    if row == 8:
        return True
        
    for col in range(8):
        if is_safe(board, row, col):
            # Place the queen
            board[row][col] = 'Q'
            
            # Recur to place the rest of the queens
            if solve_8queens(board, row + 1):
                return True
                
            # Backtrack if placing queen doesn't lead to a solution
            board[row][col] = '.'
            
    return False

# Initialize an empty 8x8 chessboard
board = [['.' for _ in range(8)] for _ in range(8)]

# Run the solver starting from row 0
if solve_8queens(board, 0):
    print("Solution found:")
    for row in board:
        print(" ".join(row))
else:
    print("Solution does not exist")