from unittest import TestCase

from cipher import Cipher


class TestStringMethods(TestCase):

    def setUp(self):
        self.cipher = Cipher()

    def test_same_case(self):
        self.assertEqual(self.cipher.encode("SS"), "SX")
