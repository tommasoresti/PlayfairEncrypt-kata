def row_checker(couple, matrix):
    return matrix.coords(couple[0])[0] == matrix.coords(couple[1])[0]


def row_encoder(couple, matrix):
    first, second = couple
    return "".join([
        matrix.letter(next_in_row(matrix.coords(first), matrix)),
        matrix.letter(next_in_row(matrix.coords(second), matrix)),
    ])


def next_in_row(coord, matrix):
    return (coord[0], 0) if coord[1] + 1 == matrix.row_len() else (coord[0], coord[1] + 1)