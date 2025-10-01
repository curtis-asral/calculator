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


def test_decimal_numbers():
    assert calculate_expression("5.5 + 4.5 * 2") == 14.5


def test_invalid_expression():
    with pytest.raises(ValueError):
        calculate_expression("2 ++ 3")
