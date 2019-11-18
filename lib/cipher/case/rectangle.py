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
