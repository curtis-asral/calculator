from calculator import add, subtract, multiply, divide


def test_addition():
    assert add(2, 3) == 5


def test_subtraction():
    assert subtract(5, 2) == 3


def test_multiplication():
    assert multiply(2, 3) == 6


def test_division():
    assert divide(6, 2) == 3
