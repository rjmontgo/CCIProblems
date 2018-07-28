import unittest

from problem_6 import compress

class TestCompress(unittest.TestCase):

    def test_single_char(self):
        self.assertEqual(compress("a"), "a")

    def test_two_chars(self):
        self.assertEqual(compress("ab"), "ab")

    def test_three_chars(self):
        self.assertEqual(compress("aab"), "aab")

    def test_three_chars_same(self):
        self.assertEqual(compress("aaa"), "a3")

    def test_random_chars_pass(self):
        self.assertEqual(compress("aaaccbbbd"), "a3c2b3d1")

    def test_long_chars_pass(self):
        self.assertEqual(compress("aaaaaaaaaabbbbbbbbbbcccc"), "a10b10c4")

    def test_random_chars_failure(self):
        self.assertEqual(compress("aaaccbbbdc"), "aaaccbbbdc")

if __name__ is '__main__':
    unittest.main()
