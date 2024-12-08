
from circle import area as circle_area, perimeter as circle_perimeter
from square import area as square_area, perimeter as square_perimeter
from triangle import area as triangle_area, perimeter as triangle_perimeter


def validate_positive(values):
    if any(v <= 0 for v in values):
        raise ValueError("All dimensions must be positive.")


def calc_circle(function, radius):
    validate_positive([radius])
    result = {
        "area": circle_area,
        "perimeter": circle_perimeter,
    }.get(function)

    if result is None:
        _raise_invalid_function(function)

    return result(radius)


def calc_square(function, side):
    validate_positive([side])
    result = {
        "area": square_area,
        "perimeter": square_perimeter,
    }.get(function)

    if result is None:
        _raise_invalid_function(function)

    return result(side)


def calc_triangle(function, sides):
    if len(sides) != 3:
        raise ValueError(f"Expected 3 arguments, got {len(sides)}.")
    validate_positive(sides)

    a, b, c = sides
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("Invalid triangle sides.")

    result = {
        "area": triangle_area,
        "perimeter": triangle_perimeter,
    }.get(function)

    if result is None:
        _raise_invalid_function(function)

    return result(a, b, c)


def calc(figure, function, size):
    calculators = {
        "circle": (calc_circle, 1),
        "square": (calc_square, 1),
        "triangle": (calc_triangle, 3),
    }

    if figure not in calculators:
        raise ValueError(f"Invalid figure: {figure}")

    calculator, expected_args = calculators[figure]

    if figure != "triangle" and len(size) != expected_args:
        raise ValueError(
            f"Expected {expected_args} argument(s) for {figure}, got {len(size)}."
        )

    return calculator(function, size if figure == "triangle" else size[0])


def _raise_invalid_function(function):
    raise ValueError(f"Invalid function: {function}")
