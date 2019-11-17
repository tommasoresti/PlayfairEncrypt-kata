from unittest import TestCase

from lib.cipher import SimpleCipher


class TestCipher(TestCase):

    def setUp(self):
        self.cipher = SimpleCipher

    def test_same_case(self):
        # self.assertEqual(len("QLGRQTVZIBTYQZ"), len(self.cipher.encode("PS. Hello, world")))
        self.assertEqual("QLGRQTVZIBTYQZ", self.cipher.encode("PS. Hello, worlds"))

