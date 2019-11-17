def column_checker(couple, matrix):
    return matrix.coords(couple[0])[1] == matrix.coords(couple[1])[1]


def column_encoder(couple):
    return couple
