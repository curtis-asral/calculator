def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


if __name__ == "__main__":
    print(
        "Welcome to the calculator! Please enter your calculations. Enter 'exit' to quit."
    )
    calculations = 1
    while True:
        prompt = input(f"Calculation {calculations}: ")
        if prompt == "exit":
            break
        symbols = ["+", "-", "*", "/"]
        symbol_dict = {"+": add, "-": subtract, "*": multiply, "/": divide}
        function = ""
        for symbol in symbols:
            if symbol in prompt:
                function = symbol
                break
        if function == "":
            print("Invalid input. Please enter a valid calculation.")
            continue
        operands = prompt.split(function)
        if len(operands) < 2:
            print("Invalid input. Please enter a valid calculation.")
            continue
        elif len(operands) > 2:
            print("Too many operands. Please enter a valid calculation.")
            continue
        try:
            x = float(operands[0].strip())
            y = float(operands[1].strip())
        except:
            print("Operands must be numbers. Please enter a valid calculation.")
            continue
        if function == "/" and y == 0:
            print("Cannot divide by zero. Please enter a valid calculation.")
            continue
        try:
            result = symbol_dict[function](x, y)
        except:
            print("Invalid input. Please enter a valid calculation.")
            continue
        print(f"Result: {result}")
        calculations += 1
