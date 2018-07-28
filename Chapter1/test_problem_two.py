import unittest

from problem_two import isPermutation

class TestIsPermutation(unittest.TestCase):
    def test_one_char_true(self):
        self.assertEqual(isPermutation("a", "a"), True)

    def test_one_char_false(self):
        self.assertEqual(isPermutation("a", "b"), False)

    def test_two_char_true(self):
        self.assertEqual(isPermutation("ab", "ba"), True)

    def test_two_chars_false(self):
        self.assertEqual(isPermutation("ac", "ab"), False)

    def test_dif_length_false(self):
        self.assertEqual(isPermutation("acc", "ac"), False)

    def test_three_chars_true(self):
        self.assertEqual(isPermutation("abc", "cab"), True)

    def test_three_chars_false(self):
        self.assertEqual(isPermutation("ftz", "dfs"), False)

if __name__ is '__main__':
    unittest.main()
