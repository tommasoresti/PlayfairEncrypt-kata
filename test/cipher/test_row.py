from unittest import TestCase

from lib.cipher.matrix import Matrix
from lib.cipher.row import row_checker, row_encoder


class TestRow(TestCase):

    def setUp(self):
        self.matrix = Matrix([
            ["B", "S", "V"],
            ["A", "R", "D"]
        ])

    def test_checker(self):
        self.assertTrue(row_checker("BS", self.matrix))
        self.assertFalse(row_checker("BA", self.matrix))

    def test_encoder(self):
        self.assertEqual(row_encoder("BS", self.matrix), "SV")
