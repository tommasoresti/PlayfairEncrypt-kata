def _all_true(checkers, couple, matrix):
    for checker in checkers:
        if not checker(couple, matrix):
            return False
    return True


def always(couple, matrix):
    return True


def all(checkers):
    return lambda couple, matrix: _all_true(checkers, couple, matrix)


def nott(checker):
    return lambda couple, matrix: not checker(couple, matrix)
