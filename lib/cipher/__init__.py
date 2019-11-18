from lib.cipher.case.generic import all, nott
from lib.cipher.case.same import is_same_letter, replace_second_with_X, duplicate_first, ends_with_X
from lib.cipher.cipher import Cipher
from lib.cipher.case.row import is_same_row, shift_right, shift_left
from lib.cipher.case.rectangle import swap_columns
from lib.cipher.case.column import is_same_column, shift_down, shift_up

CIPHER = (["D", "A", "V", "I", "O"],
          ["Y", "N", "E", "R", "B"],
          ["C", "F", "G", "H", "K"],
          ["L", "M", "P", "Q", "S"],
          ["T", "U", "W", "X", "Z"])

encoders = [
    (is_same_letter, replace_second_with_X),
    (all([nott(is_same_letter), is_same_row]), shift_right),
    (all([nott(is_same_letter), is_same_column]), shift_down),
    (all([nott(is_same_column), nott(is_same_row)]), swap_columns)
]

decoders = [
    (all([nott(is_same_letter), is_same_row]), shift_left),
    (all([nott(is_same_letter), is_same_column]), shift_up),
    (all([nott(is_same_column), nott(is_same_row)]), swap_columns),
    (ends_with_X, duplicate_first)
]

SimpleCipher = Cipher(CIPHER, encoders, decoders)
