import unittest
from calculate import calc


class TestCalc(unittest.TestCase):

    def test_circle_perimeter(self):
        fig = "circle"
        func = "perimeter"
        size = [5]
        result = calc(fig, func, size)
        self.assertAlmostEqual(result, 31.4159, places=4)

    def test_circle_area(self):
        fig = "circle"
        func = "area"
        size = [5]
        result = calc(fig, func, size)
        self.assertAlmostEqual(result, 78.5398, places=4)

    # Square tests
    def test_square_perimeter(self):
        fig = "square"
        func = "perimeter"
        size = [4]
        result = calc(fig, func, size)
        self.assertEqual(result, 16)

    def test_square_area(self):
        fig = "square"
        func = "area"
        size = [4]
        result = calc(fig, func, size)
        self.assertEqual(result, 16)

    # Triangle tests
    def test_triangle_perimeter(self):
        fig = "triangle"
        func = "perimeter"
        size = [3, 4, 5]
        result = calc(fig, func, size)
        self.assertEqual(result, 12)

    def test_triangle_area(self):
        fig = "triangle"
        func = "area"
        size = [3, 4, 5]
        result = calc(fig, func, size)
        self.assertAlmostEqual(result, 6.0, places=4)

    # Error tests
    def test_invalid_figure(self):
        fig = "hexagon"
        func = "perimeter"
        size = [3]
        with self.assertRaises(ValueError) as context:
            calc(fig, func, size)
        self.assertEqual(str(context.exception), "Invalid figure: hexagon")

    def test_invalid_function(self):
        fig = "circle"
        func = "volume"
        size = [3]
        with self.assertRaises(ValueError) as context:
            calc(fig, func, size)
        self.assertEqual(str(context.exception), "Invalid function: volume")

    def test_invalid_triangle_sides(self):
        fig = "triangle"
        func = "area"
        size = [1, 1, 10]
        with self.assertRaises(ValueError) as context:
            calc(fig, func, size)
        self.assertEqual(str(context.exception), "Invalid triangle sides.")

    def test_negative_values(self):
        fig = "circle"
        func = "area"
        size = [-5]
        with self.assertRaises(ValueError) as context:
            calc(fig, func, size)
        self.assertEqual(str(context.exception), "All dimensions must be positive.")


if __name__ == "__main__":
    unittest.main()
