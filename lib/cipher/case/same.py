def is_same_letter(couple, matrix):
    return matrix.coords(couple[0]) == matrix.coords(couple[1])


def ends_with_X(couple, matrix):
    return matrix.coords(couple[0]) == matrix.coords(couple[1])


def replace_second_with_X(couple, matrix):
    return couple[0] + 'X'


def duplicate_first(couple, matrix):
    return couple[0] + couple[0]
