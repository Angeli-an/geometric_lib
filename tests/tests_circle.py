import unittest
import math
from circle import area, perimeter


class TestGeometryFunctions(unittest.TestCase):

    def test_area_positive(self):
        radius = 5
        expected_area = math.pi * radius * radius
        result = area(radius)
        self.assertAlmostEqual(result, expected_area)

    def test_area_zero(self):
        radius = 0
        result = area(radius)
        self.assertEqual(result, 0)

    def test_area_negative(self):
        radius = -5
        with self.assertRaises(AssertionError):
            area(radius)

    def test_perimeter_positive(self):
        radius = 5
        expected_perimeter = 2 * math.pi * radius
        result = perimeter(radius)
        self.assertAlmostEqual(result, expected_perimeter)

    def test_perimeter_zero(self):
        radius = 0
        result = perimeter(radius)
        self.assertEqual(result, 0)

    def test_perimeter_negative(self):
        radius = -5
        with self.assertRaises(AssertionError):
            perimeter(radius)


if __name__ == "__main__":
    unittest.main()
