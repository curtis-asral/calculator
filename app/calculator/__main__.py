from . import calculate_expression
from app.memento import undo, redo, history, clear, clear_history
import pandas as pd
import os
from dotenv import load_dotenv

if __name__ == "__main__":
    # Load environment variables
    load_dotenv(override=True)

    # Print welcome message
    print(
        "Welcome to the calculator! Please enter your calculations. Enter 'exit' to quit."
    )

    # Run the calculator
    calculations = 1
    while True:
        try:
            df = pd.read_csv(os.getenv("history"))
        except:
            df = pd.DataFrame(columns=["equation"])

        prompt = input(f"Calculation {calculations}: ")

        if prompt.lower() == "exit":
            break
        elif prompt.lower() == "undo":
            res = undo()
            if res is not None:
                print(f"Undone: {res}")
            else:
                print("Nothing to undo")
            continue
        elif prompt.lower() == "redo":
            res = redo()
            if res is not None:
                print(f"Redone: {res}")
            else:
                print("Nothing to redo")
            continue
        elif prompt.lower() == "history":
            his = history()
            for i, eq in enumerate(his):
                print(f"{i+1}: {eq}")
            continue
        elif prompt.lower() == "help":
            print(
                "Available commands: exit, undo, redo, history, help, clear, clear_history"
            )
            continue
        elif prompt.lower() == "clear":
            clear()
            continue
        elif prompt.lower() == "clear_history":
            clear_history()
            continue

        try:
            result = calculate_expression(prompt)
            print(f"Result: {result}")
            equation = f"{prompt} = {result}"
            df.loc[len(df)] = [equation]
            df.to_csv(os.getenv("history"), index=False)
            calculations += 1
        except Exception as e:
            print(str(e))
            equation = f"{prompt} = {str(e)}"
            df.loc[len(df)] = [equation]
            df.to_csv(os.getenv("history"), index=False)
