# Define a partially filled Sudoku board
sudoku_board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

# Function to neatly print the Sudoku board
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