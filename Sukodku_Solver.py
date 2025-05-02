# Define a partially filled Sudoku board
sudoku_board = [
    [0, 0, 0, 0, 7, 0, 5, 1, 0],
    [0, 0, 7, 0, 0, 0, 0, 8, 2],
    [0, 0, 0, 9, 2, 8, 0, 0, 0],
    [0, 3, 0, 0, 0, 4, 0, 0, 0],
    [7, 9, 0, 0, 0, 0, 0, 6, 1],
    [0, 0, 0, 7, 0, 0, 0, 3, 0],
    [0, 0, 0, 4, 6, 9, 0, 0, 0],
    [2, 1, 0, 0, 0, 0, 8, 0, 0],
    [0, 5, 6, 0, 1, 0, 0, 0, 0]
]


# Function to print the Sudoku board
def print_sudoku_board(board):
    for i, row in enumerate(board):
        if i % 3 == 0 and i != 0:
            print("-" * 21)  # Print horizontal separator every 3 rows
        for j, value in enumerate(row):
            if j % 3 == 0 and j != 0:
                print("| ", end="")  # Print vertical separator every 3 columns
            print(value if value != 0 else ".", end=" ")
        print()  # Newline after each row

# Example usage
print_sudoku_board(sudoku_board)


# Function to find an empty location in the Sudoku board
def search_empty_location(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                return (col, row)
    return None  # No empty location found

print(search_empty_location(sudoku_board))


