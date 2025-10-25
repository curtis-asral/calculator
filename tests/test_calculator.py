import pytest
from app.calculator import calculate_expression


def test_simple_addition():
    assert calculate_expression("2 + 3") == 5


def test_mixed_operations():
    assert calculate_expression("2 + 3 * 4") == 14  # 3*4 first


def test_parentheses_like_behavior():
    # since no parentheses support, check precedence only
    assert calculate_expression("10 - 2 * 3") == 4


def test_division_result():
    assert calculate_expression("8 / 2 + 3") == 7
    

def test_division_by_zero():
    from app.exceptions import OperationError
    with pytest.raises(OperationError):
        calculate_expression("8 / 0")

def test_power():
    assert calculate_expression("2**3") == 8

def test_root():
    assert calculate_expression("sqrt(16)") == 4

def test_modulus():
    assert calculate_expression("7 % 3") == 1

def test_integer_division():
    assert calculate_expression("7 // 2") == 3

def test_percent():
    assert calculate_expression("100 % 5") == 0

def test_absolute_difference():
    assert calculate_expression("5 - 10") == -5  # subtraction, not abs diff


def test_decimal_numbers():
    assert calculate_expression("5.5 + 4.5 * 2") == 14.5


def test_invalid_expression():
    from app.exceptions import ValidationError
    with pytest.raises(ValidationError):
        calculate_expression("2 ++ 3")
