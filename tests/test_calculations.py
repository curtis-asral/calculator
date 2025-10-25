import pytest
from app.calculation import (
    AddCalculation,
    SubtractCalculation,
    MultiplyCalculation,
    DivideCalculation,
    PowerCalculation,
    RootCalculation,
    ModulusCalculation,
    IntegerDivideCalculation,
    PercentCalculation,
    AbsoluteDifferenceCalculation,
    CalculationFactory,
)
from app.exceptions import OperationError

import math

import pytest

@pytest.mark.parametrize(
    "cls,a,b,expected",
    [
        (AddCalculation, 2, 3, 5),
        (SubtractCalculation, 10, 4, 6),
        (MultiplyCalculation, 3, 7, 21),
        (DivideCalculation, 10, 2, 5),
        (PowerCalculation, 2, 3, 8),
        (RootCalculation, 16, 2, 4),
        (ModulusCalculation, 7, 3, 1),
        (IntegerDivideCalculation, 7, 2, 3),
        (PercentCalculation, 50, 100, 50),
        (AbsoluteDifferenceCalculation, 5, 10, 5),
        (AbsoluteDifferenceCalculation, 10, 5, 5),
    ]
)
def test_calculation_classes(cls, a, b, expected):
    calc = cls(a, b)
    result = calc.get_result()
    if isinstance(result, float) and isinstance(expected, int):
        assert math.isclose(result, expected)
    else:
        assert result == expected

@pytest.mark.parametrize(
    "cls,a,b,exception",
    [
        (DivideCalculation, 5, 0, OperationError),
    ]
)
def test_calculation_exceptions(cls, a, b, exception):
    with pytest.raises(exception):
        cls(a, b).get_result()

def test_factory_add():
    calc = CalculationFactory.create("add", 1, 2)
    assert calc.get_result() == 3

def test_factory_invalid():
    with pytest.raises(OperationError):
        CalculationFactory.create("modulo", 1, 2)
