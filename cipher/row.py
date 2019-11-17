def row_checker(couple, matrix):
    return matrix.coords(couple[0])[0] == matrix.coords(couple[1])[0]


def row_encoder(couple):
    return couple
