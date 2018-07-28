import unittest

from problem_1 import isUnique

class TestIsUnique(unittest.TestCase):
    def test_single_val(self):
        self.assertEqual(isUnique("a"), True)

    def test_two_unique_vals(self):
        self.assertEqual(isUnique("ab"), True)

    def test_three_unique_vals(self):
        self.assertEqual(isUnique("abc"), True)

    def test_three_non_unique_vals(self):
        self.assertEqual(isUnique("aba"), False)

    def test_four_unique_vals(self):
        self.assertEqual(isUnique("czq"), True)

    def test_four_non_unique_vals(self):
        self.assertEqual(isUnique("fata"), False)



if __name__ is '__main__':
    unittest.main()
