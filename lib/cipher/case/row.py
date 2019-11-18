def same_row(couple, matrix):
    return matrix.coords(couple[0])[0] == matrix.coords(couple[1])[0]


def shift_right(couple, matrix):
    first, second = couple
    return "".join([
        matrix.letter(next_in_row(matrix.coords(first), matrix)),
        matrix.letter(next_in_row(matrix.coords(second), matrix)),
    ])


def shift_left(couple, matrix):
    first, second = couple
    return "".join([
        matrix.letter(prev_in_row(matrix.coords(first), matrix)),
        matrix.letter(prev_in_row(matrix.coords(second), matrix)),
    ])


def next_in_row(coord, matrix):
    return (coord[0], 0) if coord[1] + 1 == matrix.row_len() else (coord[0], coord[1] + 1)


def prev_in_row(coord, matrix):
    return (coord[0], matrix.row_len() - 1) if coord[1] == 0 else (coord[0], coord[1] - 1)
