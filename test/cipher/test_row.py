from unittest import TestCase

from lib.cipher.matrix import Matrix
from lib.cipher.case.row import same_row, shift_right, shift_left


class TestRow(TestCase):

    def setUp(self):
        self.matrix = Matrix([
            ["B", "S", "V"],
            ["A", "R", "D"]
        ])

    def test_checker(self):
        self.assertTrue(same_row("BS", self.matrix))
        self.assertFalse(same_row("BA", self.matrix))

    def test_encoder(self):
        self.assertEqual(shift_right("BS", self.matrix), "SV")
        self.assertEqual(shift_right("SV", self.matrix), "VB")

    def test_decoder(self):
        self.assertEqual(shift_left("SV", self.matrix), "BS")
        self.assertEqual(shift_left("BS", self.matrix), "VB")
