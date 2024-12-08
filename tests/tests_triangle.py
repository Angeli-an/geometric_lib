import unittest
from triangle import area, perimeter


class TestTriangleFunctions(unittest.TestCase):

    def test_area_positive(self):
        a, b, c = 3, 4, 5
        expected_area = 6.0
        result = area(a, b, c)
        self.assertAlmostEqual(result, expected_area)

    def test_area_zero(self):
        a, b, c = 0, 0, 0
        result = area(a, b, c)
        self.assertEqual(result, 0)

    def test_area_negative(self):
        a, b, c = -3, 4, 5
        with self.assertRaises(ValueError):
            area(a, b, c)

    def test_perimeter_positive(self):
        a, b, c = 3, 4, 5
        expected_perimeter = 12
        result = perimeter(a, b, c)
        self.assertEqual(result, expected_perimeter)

    def test_perimeter_zero(self):
        a, b, c = 0, 0, 0
        result = perimeter(a, b, c)
        self.assertEqual(result, 0)

    def test_perimeter_negative(self):
        a, b, c = -3, 4, 5
        with self.assertRaises(ValueError):
            perimeter(a, b, c)


if __name__ == "__main__":
    unittest.main()
