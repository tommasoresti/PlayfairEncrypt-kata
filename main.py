import sys
import re

if len(sys.argv) != 2:
    print("No input string")
    exit()

i = sys.argv[1]

CIPHER = (("D", "A", "V", "I", "O"),
          ("Y", "N", "E", "R", "B"),
          ("C", "F", "G", "H", "K"),
          ("L", "M", "P", "Q", "S"),
          ("T", "U", "W", "X", "Z"))


i = str.upper(i)
i = re.sub(r'[^A-Z]+', "", i)


def split_couple(input, output):
    if len(input) == 0:
        return output

    if len(input) == 1:
        output.append(input + 'X')
        return output

    print(input[:2])
    output.append(input[:2])
    return split_couple(input[2:], output)


def row_case(couple):
    return couple


def column_case(couple):
    return couple


def rectangle_case(couple):
    return couple


def same_case(couple):
    return couple


def find_case(couple):
    return "same"


couples = split_couple(i, [])
encrypt_function = {
    "row": row_case,
    "column": column_case,
    "rectangle": rectangle_case,
    "same": same_case,
}


result = ""
for couple in couples:
    result += encrypt_function[find_case(couple)](couple)








