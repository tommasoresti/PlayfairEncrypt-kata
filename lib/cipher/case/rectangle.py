def rectangle_checker(couple, matrix):
    return matrix.coords(couple[0])[0] != matrix.coords(couple[1])[0] and \
           matrix.coords(couple[0])[1] != matrix.coords(couple[1])[1]


def rectangle_decoder(couple, matrix):
    return swap_columns(couple, matrix)


def swap_columns(couple, matrix):
    first, second = couple

    x1, y1 = matrix.coords(first)
    x2, y2 = matrix.coords(second)

    return "".join(
        [
            matrix.letter((x1, y2)),
            matrix.letter((x2, y1)),
        ]
    )
