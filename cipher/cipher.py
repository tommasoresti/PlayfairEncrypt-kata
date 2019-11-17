import re

from cipher.matrix import Matrix


class Cipher:
    def __init__(self, letters, encoders):
        self.encoders = encoders
        self.matrix = Matrix(letters)

    def split_couple(self, input, output):
        if len(input) == 0:
            return output

        if len(input) == 1:
            output.append(input + 'X')
            return output

        output.append(input[:2])
        return self.split_couple(input[2:], output)

    def encode(self, input_value):
        input_value = str.upper(input_value)
        input_value = re.sub(r'[^A-Z]+', "", input_value)

        couples = self.split_couple(input_value, [])

        result = ""
        for couple in couples:
            for case in self.encoders:
                if case[0](couple, self.matrix):
                    result += case[1](couple)
                    break
        return result
