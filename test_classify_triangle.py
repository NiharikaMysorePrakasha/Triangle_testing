import unittest
from classify_triangle import classify_triangle

class TestClassifyTriangle(unittest.TestCase):

    def test_equilateral(self):
        self.assertEqual(classify_triangle(3, 3, 3), "Equilateral Triangle")

    def test_isosceles(self):
        self.assertEqual(classify_triangle(5, 5, 8), "Isosceles Triangle")

    def test_scalene(self):
        self.assertEqual(classify_triangle(7, 5, 6), "Scalene Triangle")

    def test_right_triangle(self):
        self.assertEqual(classify_triangle(3, 4, 5), "Scalene Right Triangle")

    def test_isosceles_right(self):
        self.assertEqual(classify_triangle(1, 1, 1.414), "Isosceles Triangle")

    def test_invalid_sides(self):
        self.assertEqual(classify_triangle(0, 4, 5), "Invalid Triangle: Sides should be greater than 0")
        self.assertEqual(classify_triangle(1, 10, 12), "Invalid Triangle: Sides do not form a valid triangle")

if __name__ == "__main__":
    unittest.main()
