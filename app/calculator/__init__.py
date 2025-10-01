from app.calculation import CalculationFactory
import re

def calculate_expression(expression):
    symbols = ["+", "-", "*", "/"]
    symbol_dict = {"+": "add", "-": "subtract", "*": "multiply", "/": "divide"}

    # Remove whitespace
    expression = expression.replace(" ", "")
    
    # Parse the expression into tokens (numbers and operators)
    tokens = re.findall(r'\d+\.?\d*|[+\-*/]', expression)
    
    # Validate we have the right structure
    if len(tokens) < 3 or len(tokens) % 2 == 0:
        raise ValueError("Invalid expression format")
    
    # Check if parsed tokens match original expression length (catches ++)
    reconstructed = ''.join(tokens)
    if reconstructed != expression:
        raise ValueError("Invalid expression format")

    # Validate and separate tokens into numbers and operators
    try:
        numbers = []
        operators = []
        for i, token in enumerate(tokens):
            if i % 2 == 0:  # Should be a number
                numbers.append(float(token))
            else:  # Should be an operator
                if token not in symbols:
                    raise ValueError("Invalid operator")
                operators.append(token)
    except (ValueError, IndexError) as e:
        raise ValueError("Invalid expression format") from e

    # Apply order of operations: first multiply and divide
    i = 0
    while i < len(operators):
        if operators[i] in ["*", "/"]:
            calculation = CalculationFactory.create(
                symbol_dict[operators[i]], 
                numbers[i], 
                numbers[i + 1]
            )
            result = calculation.get_result()
            # Replace the two operands and operator with the result
            numbers = numbers[:i] + [result] + numbers[i + 2:]
            operators = operators[:i] + operators[i + 1:]
        else:
            i += 1

    # Then apply addition and subtraction from left to right
    i = 0
    while i < len(operators):
        calculation = CalculationFactory.create(
            symbol_dict[operators[i]], 
            numbers[i], 
            numbers[i + 1]
        )
        result = calculation.get_result()
        numbers = numbers[:i] + [result] + numbers[i + 2:]
        operators = operators[:i] + operators[i + 1:]

    result = numbers[0]
    
    # Return as int if it's a whole number, otherwise float
    return int(result) if result == int(result) else result