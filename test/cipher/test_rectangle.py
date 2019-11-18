from unittest import TestCase

from lib.cipher.matrix import Matrix
from lib.cipher.case.rectangle import swap_columns


class TestRectangle(TestCase):

    def setUp(self):
        self.matrix = Matrix([
            ["B", "S", "W"],
            ["A", "R", "P"],
            ["O", "G", "L"],
        ])

    def test_encoder(self):
        self.assertEqual(swap_columns("BR", self.matrix), "SA")
