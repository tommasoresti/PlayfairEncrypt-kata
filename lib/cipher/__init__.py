from lib.cipher.case.generic import for_all, is_not
from lib.cipher.case.same import same_letter, put_an_X, duplicate_first, ends_with_X
from lib.cipher.cipher import Cipher
from lib.cipher.case.row import same_row, shift_right, shift_left
from lib.cipher.case.rectangle import rectangle_checker, swap_columns
from lib.cipher.case.column import same_column, shift_down, shift_up

CIPHER = (["D", "A", "V", "I", "O"],
          ["Y", "N", "E", "R", "B"],
          ["C", "F", "G", "H", "K"],
          ["L", "M", "P", "Q", "S"],
          ["T", "U", "W", "X", "Z"])

encoders = [
    (same_letter, put_an_X),
    (for_all([is_not(same_letter), same_row]), shift_right),
    (for_all([is_not(same_letter), same_column]), shift_down),
    (rectangle_checker, swap_columns)
]

decoders = [
    (for_all([is_not(same_letter), same_row]), shift_left),
    (for_all([is_not(same_letter), same_column]), shift_up),
    (rectangle_checker, swap_columns),
    (ends_with_X, duplicate_first)
]

SimpleCipher = Cipher(CIPHER, encoders, decoders)
