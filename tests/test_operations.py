import pytest
from calculator import add, subtract, multiply, divide


@pytest.mark.parametrize(
    "x, y, expected",
    [
        (2, 3, 5),
        (-1, 1, 0),
        (0, 0, 0),
        (1.5, 2.5, 4.0),
        (-2, -3, -5),
        (1e10, 1e10, 2e10),
    ],
)
def test_add(x, y, expected):
    assert add(x, y) == expected


@pytest.mark.parametrize(
    "x, y, expected",
    [
        (5, 2, 3),
        (0, 1, -1),
        (-1, -1, 0),
        (2.5, 1.5, 1.0),
        (1e10, 1e9, 9e9),
    ],
)
def test_subtract(x, y, expected):
    assert subtract(x, y) == expected


@pytest.mark.parametrize(
    "x, y, expected",
    [
        (2, 3, 6),
        (-1, 1, -1),
        (0, 5, 0),
        (1.5, 2, 3.0),
        (-2, -3, 6),
        (1e5, 1e5, 1e10),
    ],
)
def test_multiply(x, y, expected):
    assert multiply(x, y) == expected


@pytest.mark.parametrize(
    "x, y, expected",
    [
        (6, 2, 3),
        (5, 2, 2.5),
        (-6, 3, -2),
        (1.5, 0.5, 3.0),
        (1e10, 2, 5e9),
    ],
)
def test_divide(x, y, expected):
    assert divide(x, y) == expected


@pytest.mark.parametrize(
    "x, y",
    [
        (5, 0),
        (0, 0),
        (-3, 0),
    ],
)
def test_divide_by_zero(x, y):
    with pytest.raises(ZeroDivisionError):
        divide(x, y)
