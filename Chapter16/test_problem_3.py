import unittest

from lib.line import Line
from problem_3 import lineIntersection

class TestLineIntersection(unittest.TestCase):

    def test_simple_line_intersection(self):
        l1 = Line((0, 0), (1, 1))
        l2 = Line((0, 1), (1, 0))

        self.assertTrue(lineIntersection(l1, l2))

    def test_parallel_lines_no_intersect(self):
        l1 = Line((0, 3), (3, 0))
        l2 = Line((0, 2), (2, 0))

        self.assertFalse(lineIntersection(l1, l2))

    def test_parallel_lines_intersect(self):
        l1 = Line((0, 3), (3, 0))
        l2 = Line((-1, 4), (4, -1))

        self.assertTrue(lineIntersection(l1, l2))

    def test_line_intersection_not_in_domain(self):
        l1 = Line((0, 3), (1, 2))
        l2 = Line((2, 1), (3, 0))

        self.assertFalse(lineIntersection(l1, l2))

if __name__ is '__main__':
    unittest.main()
