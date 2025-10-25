import logging
from app.calculation import CalculationFactory
from app.exceptions import OperationError, ValidationError
import re

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    filename="logs/calculator.log",
    filemode="a",  # 'a' means append mode, so new logs will be added to existing file
)


def calculate_expression(expression):
    symbols = ["+", "-", "*", "/", "**", "sqrt", "%", "//", "%%", "^"]
    symbol_dict = {
        "+": "add",
        "-": "subtract",
        "*": "multiply",
        "/": "divide",
        "**": "power",
        "sqrt": "root",
        "%": "modulus",
        "//": "integer_divide",
        "%%": "percent",
        "^": "absolute_difference",
    }

    logging.info(f"Received expression: {expression}")

    # Remove whitespace
    expression = expression.replace(" ", "")
    logging.debug(f"Expression after whitespace removal: {expression}")

    # Special handling for unary sqrt, e.g., sqrt(16) or sqrt16
    if expression.startswith("sqrt"):
        # Accept sqrt16 or sqrt(16)
        match = re.match(r"sqrt\(?([\d.]+)\)?", expression)
        if match:
            value = float(match.group(1))
            calculation = CalculationFactory.create("root", value, 2)
            result = calculation.get_result()
            logging.info(f"Result: {result}")
            return int(result) if result == int(result) else result
    # Build regex for all operators, sorted by length descending to match multi-char ops first
    op_regex = "|".join(
        sorted(map(re.escape, symbol_dict.keys()), key=len, reverse=True)
    )
    token_pattern = rf"\d+\.?\d*|{op_regex}"
    tokens = re.findall(token_pattern, expression)
    logging.debug(f"Parsed tokens: {tokens}")

    # Validate we have the right structure
    if len(tokens) < 3 or len(tokens) % 2 == 0:
        logging.error("Invalid expression format: wrong number of tokens")
        raise ValidationError(
            expression, "Invalid expression format"
        )  # pragma: no cover

    # Check if parsed tokens match original expression length (catches ++)
    reconstructed = "".join(tokens)
    if reconstructed != expression:
        logging.error("Invalid expression format: token reconstruction mismatch")
        raise ValidationError(
            expression, "Invalid expression format"
        )  # pragma: no cover

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
                    raise OperationError(token, "Invalid operator")
                operators.append(token)
        logging.debug(f"Numbers: {numbers}, Operators: {operators}")
    except (ValueError, IndexError) as e:
        logging.error(f"Exception during token validation: {e}")
        raise ValidationError(
            expression, "Invalid expression format"
        ) from e  # pragma: no cover

    # Operator precedence: list of lists, highest precedence first
    precedence = [
        ["**", "sqrt"],
        ["*", "/", "%", "//", "%%"],
        ["+", "-", "^"],
    ]

    # Evaluate by precedence
    for ops in precedence:
        i = 0
        while i < len(operators):
            if operators[i] in ops:
                logging.info(
                    f"Performing {operators[i]} on {numbers[i]} and {numbers[i+1] if i+1 < len(numbers) else 'N/A'}"
                )
                op_key = symbol_dict[operators[i]]
                # sqrt is unary, only uses numbers[i]
                if operators[i] == "sqrt":
                    calculation = CalculationFactory.create(op_key, numbers[i], 2)
                    result = calculation.get_result()
                    numbers = numbers[:i] + [result] + numbers[i + 1 :]
                else:
                    calculation = CalculationFactory.create(
                        op_key, numbers[i], numbers[i + 1]
                    )
                    result = calculation.get_result()
                    numbers = numbers[:i] + [result] + numbers[i + 2 :]
                logging.info(f"Result: {result}")
                operators = operators[:i] + operators[i + 1 :]
            else:
                i += 1

    result = numbers[0]
    logging.info(f"Final result: {result}")

    # Return as int if it's a whole number, otherwise float
    return int(result) if result == int(result) else result
