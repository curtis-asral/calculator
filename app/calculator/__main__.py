
from . import calculate_expression
from app.memento import undo, redo, history, clear, clear_history
import pandas as pd
import os
from dotenv import load_dotenv
from colorama import init, Fore, Style

if __name__ == "__main__":
    # Initialize colorama
    init(autoreset=True)
    # Load environment variables
    load_dotenv(override=True)

    # Print welcome message
    print(Fore.YELLOW + Style.BRIGHT + "Welcome to the calculator! Please enter your calculations. Enter 'exit' to quit.")

    # Run the calculator
    calculations = 1
    while True:
        try:
            df = pd.read_csv(os.getenv("CALCULATOR_HISTORY_DIR"))
        except:
            df = pd.DataFrame(columns=["equation"])

        prompt = input(Fore.CYAN + f"Calculation {calculations}: " + Style.RESET_ALL)

        if prompt.lower() == "exit":
            break
        elif prompt.lower() == "undo":
            res = undo()
            if res is not None:
                print(Fore.MAGENTA + f"Undone: {res}")
            else:
                print(Fore.YELLOW + "Nothing to undo")
            continue
        elif prompt.lower() == "redo":
            res = redo()
            if res is not None:
                print(Fore.MAGENTA + f"Redone: {res}")
            else:
                print(Fore.YELLOW + "Nothing to redo")
            continue
        elif prompt.lower() == "history":
            his = history()
            for i, eq in enumerate(his):
                print(Fore.CYAN + f"{i+1}: {eq}")
            continue
        elif prompt.lower() == "help":
            print(Fore.YELLOW + Style.BRIGHT + "Available commands: exit, undo, redo, history, help, clear, clear_history")
            continue
        elif prompt.lower() == "clear":
            clear()
            continue
        elif prompt.lower() == "clear_history":
            clear_history()
            continue

        try:
            result = calculate_expression(prompt)
            print(Fore.GREEN + Style.BRIGHT + f"Result: {result}")
            equation = f"{prompt} = {result}"
            df.loc[len(df)] = [equation]
            df.to_csv(os.getenv("CALCULATOR_HISTORY_DIR"), index=False)
            calculations += 1
        except Exception as e:
            print(Fore.RED + Style.BRIGHT + str(e))
            equation = f"{prompt} = {str(e)}"
            df.loc[len(df)] = [equation]
            df.to_csv(os.getenv("CALCULATOR_HISTORY_DIR"), index=False)
