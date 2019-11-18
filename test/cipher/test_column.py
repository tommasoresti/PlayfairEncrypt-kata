from unittest import TestCase

from lib.cipher.case.column import same_column, shift_down, shift_up
from lib.cipher.matrix import Matrix


class TestColumn(TestCase):

    def setUp(self):
        self.matrix = Matrix([
            ["B", "S"],
            ["A", "R"],
            ["K", "P"],
        ])

    def test_checker(self):
        self.assertTrue(same_column("BA", self.matrix))
        self.assertFalse(same_column("BR", self.matrix))

    def test_encoder(self):
        self.assertEqual(shift_down("BA", self.matrix), "AK")

    def test_encoder_wrapping(self):
        self.assertEqual(shift_down("BK", self.matrix), "AB")

    def test_decoder(self):
        self.assertEqual(shift_up("AK", self.matrix), "BA")
