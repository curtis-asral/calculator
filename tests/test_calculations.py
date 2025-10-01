import pytest
from app.calculation import (
    AddCalculation,
    SubtractCalculation,
    MultiplyCalculation,
    DivideCalculation,
    CalculationFactory,
)


def test_add_calculation():
    calc = AddCalculation(2, 3)
    assert calc.get_result() == 5


def test_subtract_calculation():
    calc = SubtractCalculation(10, 4)
    assert calc.get_result() == 6


def test_multiply_calculation():
    calc = MultiplyCalculation(3, 7)
    assert calc.get_result() == 21


def test_divide_calculation():
    calc = DivideCalculation(10, 2)
    assert calc.get_result() == 5


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        DivideCalculation(5, 0).get_result()


def test_factory_add():
    calc = CalculationFactory.create("add", 1, 2)
    assert calc.get_result() == 3


def test_factory_invalid():
    with pytest.raises(ValueError):
        CalculationFactory.create("modulo", 1, 2)
