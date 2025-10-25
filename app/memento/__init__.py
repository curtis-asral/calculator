import pandas as pd
import os


undo_stack = []


def undo():
    try:
        df = pd.read_csv(os.getenv("CALCULATOR_HISTORY_DIR"))
    except:
        df = pd.DataFrame(columns=["equation"])
    history = df["equation"].tolist()

    if len(history) > 0:
        equation = history.pop()
        df = df.iloc[:-1]
        df.to_csv(os.getenv("CALCULATOR_HISTORY_DIR"), index=False)
        undo_stack.append(equation)
        return equation
    else:
        return None


def redo():
    try:
        df = pd.read_csv(os.getenv("CALCULATOR_HISTORY_DIR"))
    except:
        df = pd.DataFrame(columns=["equation"])
    history = df["equation"].tolist()

    if len(undo_stack) > 0:
        equation = undo_stack.pop()
        df.loc[len(df)] = [equation]
        df.to_csv(os.getenv("CALCULATOR_HISTORY_DIR"), index=False)
        history.append(equation)
        return equation
    else:
        return None


def history():
    try:
        df = pd.read_csv(os.getenv("CALCULATOR_HISTORY_DIR"))
    except:
        df = pd.DataFrame(columns=["equation"])
    history = df["equation"].tolist()
    return history


def clear():
    # Check the operating system
    if os.name == "nt":  # For Windows
        os.system("cls")
    else:  # For macOS and Linux
        os.system("clear")


def clear_history():
    df = pd.DataFrame()
    df.to_csv(os.getenv("CALCULATOR_HISTORY_DIR"), index=False)
