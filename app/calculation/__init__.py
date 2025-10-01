from abc import ABC, abstractmethod
from app.operation import add, subtract, multiply, divide


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
            raise ZeroDivisionError("Division by zero is not allowed.")
        return divide(self.a, self.b)


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
        else:
            raise ValueError(f"Unknown operation: {operation}")
