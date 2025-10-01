from . import calculate_expression

if __name__ == "__main__":
    print("Welcome to the calculator! Please enter your calculations. Enter 'exit' to quit.")
    calculations = 1

    while True:
        prompt = input(f"Calculation {calculations}: ")
        if prompt.lower() == "exit":
            break
        
        try:
            result = calculate_expression(prompt)
            print(f"Result: {result}")
            calculations += 1
        except Exception as e:
            print(str(e))