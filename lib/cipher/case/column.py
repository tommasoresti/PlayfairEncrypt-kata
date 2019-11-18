def same_column(couple, matrix):
    return matrix.coords(couple[0])[1] == matrix.coords(couple[1])[1]


def shift_down(couple, matrix):
    first, second = couple
    return "".join([
        matrix.letter(next_in_col(matrix.coords(first), matrix)),
        matrix.letter(next_in_col(matrix.coords(second), matrix)),
    ])


def shift_up(couple, matrix):
    first, second = couple
    return "".join([
        matrix.letter(prev_in_col(matrix.coords(first), matrix)),
        matrix.letter(prev_in_col(matrix.coords(second), matrix)),
    ])


def next_in_col(coord, matrix):
    return (0, coord[1]) if coord[0] + 1 == matrix.column_len() else (coord[0] + 1, coord[1])


def prev_in_col(coord, matrix):
    return (matrix.column_len() - 1, coord[1]) if coord[0] == 0 else (coord[0] - 1, coord[1])
