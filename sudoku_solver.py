def solve_sudoku(board):
    row, column, solved = get_empty_coordinates(board)
    if solved:
        return True

    for value in range(1, 10):

        if value_can_be_placed(board, row, column, value):
            board[row][column] = value

            if solve_sudoku(board):
                return True

            board[row][column] = 0

    return False


def get_empty_coordinates(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j, False
    return None, None, True


def value_can_be_placed(board, row, column, value):
    return (
        valid_in_row(board, row, value)
        and valid_in_column(board, column, value)
        and valid_in_box(board, row, column, value)
    )


def valid_in_row(board, row, value):
    for i in range(9):
        if board[row][i] == value:
            return False
    return True


def valid_in_column(board, column, value):
    for i in range(9):
        if board[i][column] == value:
            return False
    return True


def valid_in_box(board, row, column, value):
    box_cord_x = row - row % 3
    box_cord_y = column - column % 3
    for i in range(3):
        for j in range(3):
            if board[box_cord_x + i][box_cord_y + j] == value:
                return False
    return True


board = [
    [3, 0, 6, 5, 0, 8, 4, 0, 0],
    [5, 2, 0, 0, 0, 0, 0, 0, 0],
    [0, 8, 7, 0, 0, 0, 0, 3, 1],
    [0, 0, 3, 0, 1, 0, 0, 8, 0],
    [9, 0, 0, 8, 6, 3, 0, 0, 5],
    [0, 5, 0, 0, 9, 0, 6, 0, 0],
    [1, 3, 0, 0, 0, 0, 2, 5, 0],
    [0, 0, 0, 0, 0, 0, 0, 7, 4],
    [0, 0, 5, 2, 0, 6, 3, 0, 0],
]

if solve_sudoku(board):
    print(*board, sep="\n")
else:
    print("no solution exists")
