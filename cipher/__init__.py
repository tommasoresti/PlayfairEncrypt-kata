from cipher.cipher import Cipher
from cipher.same import same_checker, same_encoder
from cipher.row import row_checker, row_encoder
from cipher.rectangle import rectangle_checker, rectangle_encoder
from cipher.column import column_checker, column_encoder

CIPHER = (["D", "A", "V", "I", "O"],
              ["Y", "N", "E", "R", "B"],
              ["C", "F", "G", "H", "K"],
              ["L", "M", "P", "Q", "S"],
              ["T", "U", "W", "X", "Z"])

SimpleCipher = Cipher(CIPHER, [
            (same_checker, same_encoder),
            (row_checker, row_encoder),
            (column_checker, column_encoder),
            (rectangle_checker, rectangle_encoder)
        ])
