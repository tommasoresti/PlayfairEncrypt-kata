from unittest import TestCase

from lib.cipher.case.column import column_checker, column_encoder
from lib.cipher.matrix import Matrix


class TestColumn(TestCase):

    def setUp(self):
        self.matrix = Matrix([
            ["B", "S"],
            ["A", "R"],
            ["K", "P"],
        ])

    def test_checker(self):
        self.assertTrue(column_checker("BA", self.matrix))
        self.assertFalse(column_checker("BR", self.matrix))

    def test_encoder(self):
        self.assertEqual(column_encoder("BA", self.matrix), "AK")

    def test_encoder_wrapping(self):
        self.assertEqual(column_encoder("BK", self.matrix), "AB")
