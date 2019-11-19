import re
import functools

from lib.cipher.matrix import Matrix


def split_in_couples(input_value):
    input_value = input_value + 'X' if len(input_value) % 2 == 1 else input_value
    chunksize = 2
    for pos in range(0, len(input_value), chunksize):
        yield input_value[pos:pos + chunksize]


class Cipher:
    def __init__(self, letters, encoders, decoders):
        self.encoders = encoders
        self.decoders = decoders
        self.matrix = Matrix(letters)

    def encode(self, input_value):
        input_value = str.upper(input_value)
        input_value = re.sub(r'[^A-Z]+', "", input_value)

        return functools.reduce(
            lambda accumulator, couple: accumulator + self.process(couple, self.encoders),
            split_in_couples(input_value), "")

    def decode(self, input_value):
        return functools.reduce(
            lambda accumulator, couple: accumulator + self.process(couple, self.decoders),
            split_in_couples(input_value), "")

    def process(self, couple, operations):
        process = couple
        for case in operations:
            if case[0](process, self.matrix):
                process = case[1](process, self.matrix)
        return process
