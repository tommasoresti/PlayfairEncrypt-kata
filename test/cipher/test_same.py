from unittest import TestCase

from lib.cipher.matrix import Matrix
from lib.cipher.case.same import same_checker, same_encoder


class TestSame(TestCase):

    def setUp(self):
        self.matrix = Matrix([
            ["B", "S"],
            ["A", "R"]
        ])

    def test_checker(self):
        self.assertTrue(same_checker("BB", self.matrix))
        self.assertFalse(same_checker("BA", self.matrix))

    def test_encoder(self):
        self.assertEqual(same_encoder("SS", self.matrix), "SX")
