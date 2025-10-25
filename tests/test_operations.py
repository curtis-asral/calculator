import pytest
from app.operation import (
    add,
    subtract,
    multiply,
    divide,
    power,
    root,
    modulus,
    integer_divide,
    percent,
    absolute_difference,
)

import math


@pytest.mark.parametrize(
    "func,a,b,expected",
    [
        (add, 2, 3, 5),
        (subtract, 5, 3, 2),
        (multiply, 4, 3, 12),
        (divide, 10, 2, 5),
        (divide, 7, 2, 3.5),
        (power, 2, 3, 8),
        (root, 16, 2, 4),
        (modulus, 7, 3, 1),
        (integer_divide, 7, 2, 3),
        (percent, 50, 100, 50),
        (absolute_difference, 5, 10, 5),
        (absolute_difference, 10, 5, 5),
    ],
)
def test_operations_param(func, a, b, expected):
    result = func(a, b)
    if isinstance(result, float) and isinstance(expected, int):
        assert math.isclose(result, expected)
    else:
        assert result == expected


@pytest.mark.parametrize(
    "func,a,b,exception",
    [
        (divide, 1, 0, ZeroDivisionError),
        (root, 16, 0, ZeroDivisionError),  # root(x, 0) raises ZeroDivisionError
    ],
)
def test_operations_exceptions(func, a, b, exception):
    with pytest.raises(exception):
        func(a, b)
