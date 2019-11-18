from lib.cipher.case.generic import for_all, is_not
from lib.cipher.case.same import same_checker, same_encoder
from lib.cipher.cipher import Cipher
from lib.cipher.case.row import row_checker, row_encoder
from lib.cipher.case.rectangle import rectangle_checker, rectangle_encoder
from lib.cipher.case.column import column_checker, column_encoder

CIPHER = (["D", "A", "V", "I", "O"],
              ["Y", "N", "E", "R", "B"],
              ["C", "F", "G", "H", "K"],
              ["L", "M", "P", "Q", "S"],
              ["T", "U", "W", "X", "Z"])

SimpleCipher = Cipher(CIPHER, [
            (same_checker, same_encoder),
            (for_all([is_not(same_checker), row_checker]), row_encoder),
            (for_all([is_not(same_checker), column_checker]), column_encoder),
            (rectangle_checker, rectangle_encoder)
        ])
