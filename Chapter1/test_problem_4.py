import unittest

from problem_4 import isPalinPerm

class TestIsPalinPerm(unittest.TestCase):
    def test_one_char(self):
        self.assertEqual(isPalinPerm("a"), True)

    def test_two_chars(self):
        self.assertEqual(isPalinPerm("ab"), True)

    def test_three_chars_true(self):
        self.assertEqual(isPalinPerm("aba"), True)

    def test_three_chars_false(self):
        self.assertEqual(isPalinPerm("acd"), False)

    def test_four_chars_true(self):
        self.assertEqual(isPalinPerm("adad"), True)

    def test_four_chars_false(self):
        self.assertEqual(isPalinPerm("adcd"), False)

    def test_no_chars(self):
        self.assertEqual(isPalinPerm(""), True)

    def test_all_spaces(self):
        self.assertEqual(isPalinPerm("   "), True)
if __name__ is '__main__':
    unittest.main()
