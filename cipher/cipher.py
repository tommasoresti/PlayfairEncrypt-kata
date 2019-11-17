import re


class Cipher:
    CIPHER = (["D", "A", "V", "I", "O"],
              ["Y", "N", "E", "R", "B"],
              ["C", "F", "G", "H", "K"],
              ["L", "M", "P", "Q", "S"],
              ["T", "U", "W", "X", "Z"])

    CIPHER_COORDS = {}

    def __init__(self):
        for row in range(len(self.CIPHER)):
            for col in range(len(self.CIPHER[row])):
                self.CIPHER_COORDS[self.CIPHER[row][col]] = (row, col)

    def split_couple(self, input, output):
        if len(input) == 0:
            return output

        if len(input) == 1:
            output.append(input + 'X')
            return output

        output.append(input[:2])
        return self.split_couple(input[2:], output)

    def coords(self, letter):
        return self.CIPHER_COORDS[letter]

    def row_case_checker(self, couple):
        return self.coords(couple[0])[0] == self.coords(couple[1])[0]

    def row_case(self, couple):
        return couple

    def column_case_checker(self, couple):
        return self.coords(couple[0])[1] == self.coords(couple[1])[1]

    def column_case(self, couple):
        return couple

    def else_case_checker(self, couple):
        return True

    def rectangle_case(self, couple):
        return couple

    def same_case_checker(self, couple):
        return self.coords(couple[0]) == self.coords(couple[1])

    def same_case(self, couple):
        return couple[0] + 'X'

    def encode(self, input_value):
        input_value = str.upper(input_value)
        input_value = re.sub(r'[^A-Z]+', "", input_value)

        couples = self.split_couple(input_value, [])

        encrypt_cases = [
            (self.same_case_checker, self.same_case),
            (self.row_case_checker, self.row_case),
            (self.column_case_checker, self.column_case),
            (self.else_case_checker, self.rectangle_case)
        ]

        result = ""
        for couple in couples:
            for case in encrypt_cases:
                if case[0](couple):
                    result += case[1](couple)
                    break
        return result
