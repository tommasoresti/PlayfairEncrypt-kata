def _all_true(checkers, couple, matrix):
    for checker in checkers:
        if not checker(couple, matrix):
            return False
    return True


def is_not(checker):
    return lambda couple, matrix: not checker(couple, matrix)


def for_all(checkers):
    return lambda couple, matrix: _all_true(checkers, couple, matrix)
