from unittest import TestCase

from lib.cipher.matrix import Matrix
from lib.cipher.case.same import is_same_letter, replace_second_with_X


class TestSame(TestCase):

    def setUp(self):
        self.matrix = Matrix([
            ["B", "S"],
            ["A", "R"]
        ])

    def test_checker(self):
        self.assertTrue(is_same_letter("BB", self.matrix))
        self.assertFalse(is_same_letter("BA", self.matrix))

    def test_encoder(self):
        self.assertEqual(replace_second_with_X("SS", self.matrix), "SX")
