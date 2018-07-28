import unittest

from problem_seven import rotate

class TestRotate(unittest.TestCase):

    def test_one_by_one(self):
        self.assertEquals(rotate([[1]]), [[1]])

    def test_two_by_two(self):
        self.assertEquals(rotate([
        [1, 2],
        [3, 4]
        ]),[
        [3, 1],
        [4, 2]
        ])

    def test_three_by_three(self):
        self.assertEquals(rotate([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
        ]),[
        [7, 4, 1],
        [8, 5, 2],
        [9, 6, 3]
        ])

    def test_four_by_four(self):
        self.assertEquals(rotate([
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
        ]),[
        [13, 9, 5, 1],
        [14, 10, 6, 2],
        [15, 11, 7, 3],
        [16, 12, 8, 4]
        ])

    def test_five_by_five(self):
        self.assertEquals(rotate([
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20],
        [21, 22, 23, 24, 25]
        ]),[
        [21, 16, 11, 6, 1],
        [22, 17, 12, 7, 2],
        [23, 18, 13, 8, 3],
        [24, 19, 14, 9, 4],
        [25, 20, 15, 10, 5]
        ])

if __name__ is '__main__':
    unittest.main()
