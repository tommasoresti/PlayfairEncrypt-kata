from unittest import TestCase

from cipher.matrix import Matrix
from cipher.rectangle import rectangle_checker, rectangle_encoder


class TestRectangle(TestCase):

    def setUp(self):
        self.matrix = Matrix([
            ["B", "S"],
            ["A", "R"]
        ])

    def test_checker(self):
        self.assertTrue(rectangle_checker("BR", self.matrix))
        self.assertFalse(rectangle_checker("BS", self.matrix))

    def test_encoder(self):
        self.assertEqual(rectangle_encoder("SS"), "SS")
