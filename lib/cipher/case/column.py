def column_checker(couple, matrix):
    return matrix.coords(couple[0])[1] == matrix.coords(couple[1])[1]


def column_encoder(couple, matrix):
    first, second = couple
    return "".join([
        matrix.letter(next_in_col(matrix.coords(first), matrix)),
        matrix.letter(next_in_col(matrix.coords(second), matrix)),
    ])


def next_in_col(coord, matrix):
    return (0, coord[1]) if coord[0] + 1 == matrix.column_len() else (coord[0] + 1, coord[1])
