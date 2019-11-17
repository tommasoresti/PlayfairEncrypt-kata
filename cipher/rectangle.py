def rectangle_checker(couple, matrix):
    return matrix.coords(couple[0])[0] != matrix.coords(couple[1])[0] and \
           matrix.coords(couple[0])[1] != matrix.coords(couple[1])[1]


def rectangle_encoder(couple):
    return couple
