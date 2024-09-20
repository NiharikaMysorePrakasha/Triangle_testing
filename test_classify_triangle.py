import unittest
from classify_triangle import classify_triangle

class TestClassifyTriangle(unittest.TestCase):

    def test_equilateral(self):
        result = classify_triangle(3, 3, 3)
        print(f"Testing Equilateral Triangle is ok: {result}")
        self.assertEqual(result, "Equilateral Triangle")

    def test_isosceles(self):
        result = classify_triangle(5, 5, 8)
        print(f"Testing Isosceles Triangle is ok: {result}")
        self.assertEqual(result, "Isosceles Triangle")

    def test_scalene(self):
        result = classify_triangle(7, 5, 6)
        print(f"Testing Scalene Triangle is ok: {result}")
        self.assertEqual(result, "Scalene Triangle")

    def test_right_triangle(self):
        result = classify_triangle(3, 4, 5)
        print(f"Testing Right Triangle is ok: {result}")
        self.assertEqual(result, "Scalene Right Triangle")

    def test_isosceles_right(self):
        result = classify_triangle(1, 1, 1.414)
        print(f"Testing Isosceles Right Triangle is ok: {result}")
        self.assertEqual(result, "Isosceles Triangle")

    def test_invalid_sides(self):
        result = classify_triangle(0, 4, 5)
        print(f"Testing Invalid Sides (Zero): {result}")
        self.assertEqual(result, "Invalid Triangle: Sides should be greater than 0")

        result = classify_triangle(1, 10, 12)
        print(f"Testing Invalid Triangle (Sides do not form a triangle): {result}")
        self.assertEqual(result, "Invalid Triangle: Sides do not form a valid triangle")

if __name__ == "__main__":
    unittest.main()
