from abc import ABC, abstractmethod
from app.exceptions import OperationError
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


class Calculation(ABC):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    @abstractmethod
    def execute(self):
        pass

    def get_result(self):
        return self.execute()


class AddCalculation(Calculation):
    def execute(self):
        return add(self.a, self.b)


class SubtractCalculation(Calculation):
    def execute(self):
        return subtract(self.a, self.b)


class MultiplyCalculation(Calculation):
    def execute(self):
        return multiply(self.a, self.b)


class DivideCalculation(Calculation):
    def execute(self):
        if self.b == 0:
            raise OperationError(self.b, "Division by zero is not allowed.")
        return divide(self.a, self.b)


class PowerCalculation(Calculation):
    def execute(self):
        return power(self.a, self.b)


class RootCalculation(Calculation):
    def execute(self):
        return root(self.a, self.b)


class ModulusCalculation(Calculation):
    def execute(self):
        return modulus(self.a, self.b)


class IntegerDivideCalculation(Calculation):
    def execute(self):
        return integer_divide(self.a, self.b)


class PercentCalculation(Calculation):
    def execute(self):
        return percent(self.a, self.b)


class AbsoluteDifferenceCalculation(Calculation):
    def execute(self):
        return absolute_difference(self.a, self.b)


class CalculationFactory:
    @staticmethod
    def create(operation: str, a, b):
        operation = operation.lower()
        if operation == "add":
            return AddCalculation(a, b)
        elif operation == "subtract":
            return SubtractCalculation(a, b)
        elif operation == "multiply":
            return MultiplyCalculation(a, b)
        elif operation == "divide":
            return DivideCalculation(a, b)
        elif operation == "power":
            return PowerCalculation(a, b)
        elif operation == "root":
            return RootCalculation(a, b)
        elif operation == "modulus":
            return ModulusCalculation(a, b)
        elif operation == "integer_divide":
            return IntegerDivideCalculation(a, b)
        elif operation == "percent":
            return PercentCalculation(a, b)
        elif operation == "absolute_difference":
            return AbsoluteDifferenceCalculation(a, b)
        else:
            from app.exceptions import OperationError
            raise OperationError(operation, f"Unknown operation")  # pragma: no cover
