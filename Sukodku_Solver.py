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




# Function to find an empty location in the Sudoku board
def search_empty_location(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                return (row, col)
    return None




def check_validity_number(board, num, pos):
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False
        
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] !=i:
            return False
        
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == num and (i,j) != pos:
                return False
            
    return True



def solve(board):
    find = search_empty_location(board)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if check_validity_number(board, i, (row, col)):
            board[row][col] = i

            if solve(board):
                return True

            board[row][col] = 0

    return False


def main():
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

    if solve(sudoku_board):
        print_sudoku_board(sudoku_board)
    else:
        print("No solution exists")
    
if __name__ == "__main__":
    main()