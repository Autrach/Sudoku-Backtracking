def solve_sudoku(board):
    # empty_row, empty_column = find_empty_coordinates(board)
    pass


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
