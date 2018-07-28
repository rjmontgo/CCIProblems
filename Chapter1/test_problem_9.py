import unittest

from problem_9 import isRotation

class TestIsRotation(unittest.TestCase):

    def test_one_char(self):
        self.assertEqual(isRotation("a", "a"), True)

    def test_two_chars(self):
        self.assertEqual(isRotation("ab", "ab"), True)

    def test_watermelon(self):
        self.assertEqual(isRotation("watermelon", "lonwaterme"), True)

    def test_reduce(self):
        self.assertEqual(isRotation("reduce", "ucered"), True)

    def test_waterbottle(self):
        self.assertEqual(isRotation("waterbottle", "erbottlewat"), True)

    def test_testin_fail(self):
        self.assertEqual(isRotation("testing", "testin"), False)

    def test_tesiting_fail(self):
        self.assertEqual(isRotation("testing", "tesiting"), False)


if __name__ is '__main__':
    unittest.main()
