import logging
from app.calculation import CalculationFactory
import re

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

def calculate_expression(expression):
    symbols = ["+", "-", "*", "/"]
    symbol_dict = {"+": "add", "-": "subtract", "*": "multiply", "/": "divide"}

    logging.info(f"Received expression: {expression}")

    # Remove whitespace
    expression = expression.replace(" ", "")
    logging.debug(f"Expression after whitespace removal: {expression}")
    
    # Parse the expression into tokens (numbers and operators)
    tokens = re.findall(r'\d+\.?\d*|[+\-*/]', expression)
    logging.debug(f"Parsed tokens: {tokens}")
    
    # Validate we have the right structure
    if len(tokens) < 3 or len(tokens) % 2 == 0:
        logging.error("Invalid expression format: wrong number of tokens")
        raise ValueError("Invalid expression format")
    
    # Check if parsed tokens match original expression length (catches ++)
    reconstructed = ''.join(tokens)
    if reconstructed != expression:
        logging.error("Invalid expression format: token reconstruction mismatch")
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
                    logging.error(f"Invalid operator: {token}")
                    raise ValueError("Invalid operator")
                operators.append(token)
        logging.debug(f"Numbers: {numbers}, Operators: {operators}")
    except (ValueError, IndexError) as e:
        logging.error(f"Exception during token validation: {e}")
        raise ValueError("Invalid expression format") from e

    # Apply order of operations: first multiply and divide
    i = 0
    while i < len(operators):
        if operators[i] in ["*", "/"]:
            logging.info(f"Performing {operators[i]} on {numbers[i]} and {numbers[i+1]}")
            calculation = CalculationFactory.create(
                symbol_dict[operators[i]], 
                numbers[i], 
                numbers[i + 1]
            )
            result = calculation.get_result()
            logging.info(f"Result: {result}")
            # Replace the two operands and operator with the result
            numbers = numbers[:i] + [result] + numbers[i + 2:]
            operators = operators[:i] + operators[i + 1:]
        else:
            i += 1

    # Then apply addition and subtraction from left to right
    i = 0
    while i < len(operators):
        logging.info(f"Performing {operators[i]} on {numbers[i]} and {numbers[i+1]}")
        calculation = CalculationFactory.create(
            symbol_dict[operators[i]], 
            numbers[i], 
            numbers[i + 1]
        )
        result = calculation.get_result()
        logging.info(f"Result: {result}")
        numbers = numbers[:i] + [result] + numbers[i + 2:]
        operators = operators[:i] + operators[i + 1:]

    result = numbers[0]
    logging.info(f"Final result: {result}")
    
    # Return as int if it's a whole number, otherwise float
    return int(result) if result == int(result) else result