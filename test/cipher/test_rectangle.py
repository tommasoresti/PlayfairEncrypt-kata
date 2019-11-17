from unittest import TestCase

from lib.cipher.matrix import Matrix
from lib.cipher.rectangle import rectangle_checker, rectangle_encoder


class TestRectangle(TestCase):

    def setUp(self):
        self.matrix = Matrix([
            ["B", "S", "W"],
            ["A", "R", "P"],
            ["O", "G", "L"],
        ])

    def test_checker(self):
        self.assertTrue(rectangle_checker("BR", self.matrix))
        self.assertFalse(rectangle_checker("BS", self.matrix))

    def test_encoder(self):
        self.assertEqual(rectangle_encoder("BR", self.matrix), "SA")
