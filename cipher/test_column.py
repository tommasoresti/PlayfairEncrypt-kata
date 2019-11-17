from unittest import TestCase

from cipher import column_checker, column_encoder
from cipher.matrix import Matrix


class TestColumn(TestCase):

    def setUp(self):
        self.matrix = Matrix([
            ["B", "S"],
            ["A", "R"]
        ])

    def test_checker(self):
        self.assertTrue(column_checker("BA", self.matrix))
        self.assertFalse(column_checker("BR", self.matrix))

    def test_encoder(self):
        self.assertEqual(column_encoder("SS"), "SS")
