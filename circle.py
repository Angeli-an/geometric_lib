import math


def area(radius):
    if radius < 0:
        raise AssertionError("Радиус не может быть отрицательным")
    return math.pi * radius * radius


def perimeter(radius):
    if radius < 0:
        raise AssertionError("Радиус не может быть отрицательным")
    return 2 * math.pi * radius
