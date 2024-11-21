import math
import unittest

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return f"Point{self}"

    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)

    def __ne__(self, other):
        return (self.x,self.y) != (other.x,other.y)

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return self.x * other.x + self.y * other.y

    def cross(self, other):
        return self.x * other.y - self.y * other.x

    def length(self):
        return math.sqrt(self.x**2 + self.y**2)

    def __hash__(self):
        return hash((self.x, self.y))


class TestPoint(unittest.TestCase):
    def test__str__(self):
        p = Point(1, 5)
        p2 = Point(5, 6)
        p3 = Point(12, -6)
        self.assertEqual(str(p), "(1, 5)")
        self.assertEqual(str(p2), "(5, 6)")
        self.assertEqual(str(p3), "(12, -6)")

    def test__repr__(self):
        p1 = Point(8, 9)
        p2 = Point(1, 16)
        p3 = Point(-3, 1)

        self.assertEqual(repr(p1), "Point(8, 9)")
        self.assertEqual(repr(p2), "Point(1, 16)")
        self.assertEqual(repr(p3), "Point(-3, 1)")

    def test__eq__(self):
        p1 = Point(1, 2)
        p2 = Point(1, 2)

        p3 = Point(7, 8)
        p4 = Point(1, 2)

        p5 = Point(3, 2)
        p6 = Point(1, 0)

        self.assertTrue(p1 == p2)
        self.assertFalse(p3 == p4)
        self.assertFalse(p5 == p6)

    def test__ne__(self):
        p1 = Point(1, 2)
        p2 = Point(1, 2)

        p3 = Point(7, 8)
        p4 = Point(1, 2)

        p5 = Point(3, 2)
        p6 = Point(1, 0)

        self.assertFalse(p1 != p2)
        self.assertTrue(p3 != p4)
        self.assertTrue(p5 != p6)


    def test__add__(self):
        p1 = Point(1, 2)
        p2 = Point(3, 4)
        self.assertEqual(p1 + p2, Point(4, 6))

    def test__sub__(self):
        p1 = Point(3, 4)
        p2 = Point(1, 2)
        self.assertEqual(p1 - p2, Point(2, 2))

    def test__mul__(self):
        p1 = Point(1, 2)
        p2 = Point(3, 4)
        self.assertEqual(p1 * p2, 11)

    def test_cross(self):
        p1 = Point(1, 2)
        p2 = Point(3, 4)
        self.assertEqual(p1.cross(p2), -2)

    def test_length(self):
        p = Point(3, 4)
        self.assertEqual(p.length(), 5.0)

    def test_hash(self):
        p1 = Point(3, 4)
        p2 = Point(1, 8)
        p3 = Point(3, 4)
        p4 = Point(1, 9)

        self.assertTrue(hash(p1) == hash(p3))
        self.assertTrue(hash(p2) != hash(p4))


if __name__ == "__main__":
    unittest.main()