def same_checker(couple, matrix):
    return matrix.coords(couple[0]) == matrix.coords(couple[1])


def same_encoder(couple, matrix):
    return couple[0] + 'X'
