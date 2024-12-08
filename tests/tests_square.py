import unittest
from square import area, perimeter


class TestGeometryFunctions(unittest.TestCase):

    def test_area_with_positive_side(self):
        side = 4
        result = area(side)
        self.assertEqual(result, 16.0)

    def test_area_with_zero_side(self):
        side = 0
        result = area(side)
        self.assertEqual(result, 0.0)

    def test_area_with_negative_side(self):
        side = -4
        with self.assertRaises(ValueError):
            area(side)

    def test_perimeter_with_positive_side(self):
        side = 4
        result = perimeter(side)
        self.assertEqual(result, 16)

    def test_perimeter_with_zero_side(self):
        side = 0
        result = perimeter(side)
        self.assertEqual(result, 0)

    def test_perimeter_with_negative_side(self):
        side = -4
        with self.assertRaises(ValueError):
            perimeter(side)


if __name__ == "__main__":
    unittest.main()
