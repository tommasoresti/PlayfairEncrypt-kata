from unittest import TestCase

from lib.cipher import SimpleCipher


class TestCipher(TestCase):

    def setUp(self):
        self.cipher = SimpleCipher

    def test_encode_ac(self):
        self.assertEqual("QLGRQTVZIBTYQZ", self.cipher.encode("PS. Hello, worlds"))


    def test_decode_ac(self):
        self.assertEqual("PSHELXOWORLDSX", self.cipher.decode("QLGRQTVZIBTYQZ"))
