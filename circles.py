import math

from points import Point

class Circle:

    def __init__(self, x, y, radius):
        if radius < 0:
            raise ValueError("promień ujemny")
        self.pt = Point(x, y)
        self.radius = radius

    def __repr__(self):
        return f"Circle({self.pt.x}, {self.pt.y}, {self.radius})"

    def __eq__(self, other):
        return self.pt == other.pt and self.radius == other.radius

    def __ne__(self, other):
        return not self == other

    def area(self):          # pole powierzchni
        return math.pi * self.radius ** 2

    def move(self, x, y):     # przesuniecie o (x, y)
        return Circle(self.pt.x + x, self.pt.y + y, self.radius)

    def cover(self, other): # najmniejszy okrąg pokrywający oba
        distance = math.sqrt((self.pt.x - other.pt.x) ** 2 + (self.pt.y - other.pt.y) ** 2)
        if distance + other.radius <= self.radius:
            return self
        if distance + self.radius <= other.radius:
            return other
        new_radius = (distance + self.radius + other.radius) / 2

        dx = other.pt.x - self.pt.x
        dy = other.pt.y - self.pt.y
        factor = (new_radius - self.radius) / distance if distance != 0 else 0
        new_x = self.pt.x + dx * factor
        new_y = self.pt.y + dy * factor
        return Circle(new_x, new_y, new_radius)




import unittest

class TestCircle(unittest.TestCase):

    def test__init__(self):
        circle = Circle(0, 0, 5)
        self.assertEqual(circle.pt.x, 0)
        self.assertEqual(circle.pt.y, 0)
        self.assertEqual(circle.radius, 5)

    def test__init__invalid_radius(self):
        with self.assertRaises(ValueError):
            Circle(0, 0, -5)

    def test__repr__(self):
        circle = Circle(1, 2, 3)
        self.assertEqual(repr(circle), "Circle(1, 2, 3)")

    def test__eq__(self):
        circle1 = Circle(0, 0, 5)
        circle2 = Circle(0, 0, 5)
        circle3 = Circle(1, 1, 5)
        self.assertTrue(circle1 == circle2)
        self.assertFalse(circle1 == circle3)

    def test__ne__(self):
        circle1 = Circle(0, 0, 5)
        circle2 = Circle(0, 0, 5)
        circle3 = Circle(1, 1, 5)
        self.assertFalse(circle1 != circle2)
        self.assertTrue(circle1 != circle3)

    def test_area(self):
        circle = Circle(0, 0, 5)
        expected_area = math.pi * 5**2
        self.assertEqual(circle.area(), expected_area)

    def test_move(self):
        circle = Circle(0, 0, 5)
        moved_circle = circle.move(2, 3)
        self.assertEqual(moved_circle.pt.x, 2)
        self.assertEqual(moved_circle.pt.y, 3)
        self.assertEqual(moved_circle.radius, 5)

        circle2 = Circle(1, 6, 7)
        moved_circle2 = circle2.move(6, 4)
        self.assertEqual(moved_circle2.pt.x, 7)
        self.assertEqual(moved_circle2.pt.y, 10)
        self.assertEqual(moved_circle2.radius, 7)

    def test_cover(self):
        circle1 = Circle(0, 0, 1)
        circle2 = Circle(2, 0, 1)
        covered_circle = circle1.cover(circle2)
        self.assertEqual(covered_circle.pt.x, 1)
        self.assertEqual(covered_circle.pt.y, 0)
        self.assertEqual(covered_circle.radius, 2)

        # Gdy okręgi się nie przecinają
        circle3 = Circle(-1, 0, 1)
        circle4 = Circle(3, 0, 1)
        covered_circle2 = circle3.cover(circle4)
        self.assertEqual(covered_circle2.pt.x, 1)
        self.assertEqual(covered_circle2.pt.y, 0)
        self.assertEqual(covered_circle2.radius, 3)

        # Gdy okręgi się przecinają
        circle5 = Circle(-2, 0, 2)
        circle6 = Circle(0, 0, 1)
        covered_circle3 = circle5.cover(circle6)
        self.assertEqual(covered_circle3.pt.x, -1.5)
        self.assertEqual(covered_circle3.pt.y, 0)
        self.assertEqual(covered_circle3.radius, 2.5)




if __name__ == '__main__':
    unittest.main()