from unittest import TestCase

from lib.cipher.matrix import Matrix
from lib.cipher.case.same import same_letter, put_an_X


class TestSame(TestCase):

    def setUp(self):
        self.matrix = Matrix([
            ["B", "S"],
            ["A", "R"]
        ])

    def test_checker(self):
        self.assertTrue(same_letter("BB", self.matrix))
        self.assertFalse(same_letter("BA", self.matrix))

    def test_encoder(self):
        self.assertEqual(put_an_X("SS", self.matrix), "SX")
