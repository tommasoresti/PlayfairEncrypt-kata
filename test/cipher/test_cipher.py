from unittest import TestCase

from lib.cipher import SimpleCipher


class TestCipher(TestCase):

    def setUp(self):
        self.cipher = SimpleCipher

    def test_encode_ac(self):
        self.assertEqual("QLGRQTVZIBTYQZ", self.cipher.encode("PS. Hello, worlds"))
        self.assertEqual("RI", self.cipher.encode("IJ"))

    def test_decode_ac(self):
        self.assertEqual("PSHELXOWORLDSX", self.cipher.decode("QLGRQTVZIBTYQZ"))
        self.assertEqual("IX", self.cipher.decode("RI"))
