from unittest import TestCase

from lib.cipher.case.generic import nott, all
from lib.cipher.matrix import Matrix


class TestGeneric(TestCase):

    def setUp(self):
        self.matrix = Matrix([])

    def test_all(self):
        self.assertTrue(all([lambda foo, bar: True, lambda foo, bar: True])("", self.matrix))
        self.assertFalse(all([lambda foo, bar: True, lambda foo, bar: False])("", self.matrix))
        self.assertFalse(all([lambda foo, bar: False, lambda foo, bar: True])("", self.matrix))
        self.assertFalse(all([lambda foo, bar: False, lambda foo, bar: False])("", self.matrix))

    def test_nott(self):
        self.assertTrue(nott(lambda foo, bar: False)("", self.matrix))
