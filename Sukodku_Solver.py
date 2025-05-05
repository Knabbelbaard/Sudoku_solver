from flask import Flask, render_template, request

app = Flask(__name__)
    

# sudoku_board = [
    #     [0, 0, 0, 0, 7, 0, 5, 1, 0],
    #     [0, 0, 7, 0, 0, 0, 0, 8, 2],
    #     [0, 0, 0, 9, 2, 8, 0, 0, 0],
    #     [0, 3, 0, 0, 0, 4, 0, 0, 0],
    #     [7, 9, 0, 0, 0, 0, 0, 6, 1],
    #     [0, 0, 0, 7, 0, 0, 0, 3, 0],
    #     [0, 0, 0, 4, 6, 9, 0, 0, 0],
    #     [2, 1, 0, 0, 0, 0, 8, 0, 0],
    #     [0, 5, 6, 0, 1, 0, 0, 0, 0]
    # ]


def create_sudoku_board(values):
    return [values[i:i+9] for i in range(0, 81, 9)]


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        values = request.form.getlist('cel')
        sudoku_board = create_sudoku_board([int(v) if v.isdigit() else 0 for v in values])
    else:
        sudoku_board = [[0]*9 for _ in range(9)]
    board_str = create_sudoku_board(sudoku_board)
    return render_template("index.html", board=board_str)
    
    # if solve(sudoku_board):
    #     board_str = print_sudoku_board(sudoku_board)
    #     return render_template("index.html", board=board_str)
    # else:
    #     return "No solution exists"
    


# Function to print the Sudoku board
#  def print_sudoku_board(board):
#     board_str = ""
#     for i, row in enumerate(board):
#         if i % 3 == 0 and i != 0:
#             board_str += "-" * 21 + "\n"
#         for j, value in enumerate(row):
#             if j % 3 == 0 and j != 0:
#                 board_str += "| "
#             board_str += str(value if value != 0 else ".") + " "
#         board_str += "\n"
#     return board_str


# Function to find an empty location in the Sudoku board
def search_empty_location(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                return (row, col)
    return None


# Function to check if the new number is in a valid position
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


# Function to solve the empty positions on the board
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

    
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=80)