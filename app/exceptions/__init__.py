class OperationError(Exception):
    def __init__(self, value, message="Invalid operation"):
        self.value = value
        self.message = message
        super().__init__(f"{self.message}: {self.value}")


class ValidationError(Exception):
    def __init__(self, value, message="Invalid value"):
        self.value = value
        self.message = message
        super().__init__(f"{self.message}: {self.value}")
