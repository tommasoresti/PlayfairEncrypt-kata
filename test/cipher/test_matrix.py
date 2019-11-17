from unittest import TestCase

from lib.cipher.matrix import Matrix


class TestMatrix(TestCase):

    def test_inverse_dic(self):
        to_test = (["A", "B"],
                   ["C", "D"])

        matrix = Matrix(to_test)

        self.assertEqual(matrix.coords("A"), (0, 0))
        self.assertEqual(matrix.coords("B"), (0, 1))
        self.assertEqual(matrix.coords("C"), (1, 0))
        self.assertEqual(matrix.coords("D"), (1, 1))

        self.assertEqual(matrix.letter((0, 0)), "A")
        self.assertEqual(matrix.letter((0, 1)), "B")
        self.assertEqual(matrix.letter((1, 0)), "C")
        self.assertEqual(matrix.letter((1, 1)), "D")


