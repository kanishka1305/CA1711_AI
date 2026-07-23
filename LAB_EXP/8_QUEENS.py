# Function to print the chessboard
def print_board(board):
    for row in board:
        print(" ".join("Q" if cell else "." for cell in row))
    print()


# Function to check whether it is safe to place a queen
def is_safe(board, row, col):
    # Check left side of current row
    for i in range(col):
        if board[row][i]:
            return False

    # Check upper-left diagonal
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j]:
            return False
        i -= 1
        j -= 1

    # Check lower-left diagonal
    i, j = row, col
    while i < 8 and j >= 0:
        if board[i][j]:
            return False
        i += 1
        j -= 1

    return True


# Backtracking function
def solve(board, col):
    if col >= 8:
        return True

    for row in range(8):
        if is_safe(board, row, col):
            board[row][col] = 1

            if solve(board, col + 1):
                return True

            # Backtrack
            board[row][col] = 0

    return False


# Main Program
board = [[0 for _ in range(8)] for _ in range(8)]

if solve(board, 0):
    print("Solution:")
    print_board(board)
else:
    print("No solution exists.")
