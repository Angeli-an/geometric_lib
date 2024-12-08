def area(a, b, c):

    if a < 0 or b < 0 or c < 0:
        raise ValueError("Сторона не может быть отрицательной")
    s = (a + b + c) / 2
    return (s * (s - a) * (s - b) * (s - c)) ** 0.5


def perimeter(a, b, c):

    if a < 0 or b < 0 or c < 0:
        raise ValueError("Сторона не может быть отрицательной")
    return a + b + c
