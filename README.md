# calculator

## Setup

**Initialize virtual environment:**
```bash
python -m venv venv
```

**Activate virtual environment:**
```bash
source venv/bin/activate
```

**Install requirements:**
```bash
pip install -r requirements.txt
```

## Running Tests

**Run all tests (including parameterized and expression tests):**
```bash
pytest -v
```

- Tests now cover various input scenarios for calculator operations and expression parsing.
- Expression tests are located in `tests/test_calculator.py`.

## Running the Calculator

**Start the calculator app:**
```bash
python -m app.calculator
```

- The calculator now supports full expression parsing (e.g., `2 + 3 * 4`).
- Logging is enabled for calculation steps and errors.
- Input expressions are validated for correct format and operator usage.

## Features

- Supports addition, subtraction, multiplication, and division.
- Handles operator precedence (multiplication/division before addition/subtraction).
- Returns integer results when possible, otherwise float.
- Logs calculation steps and errors for easier debugging.
- Raises clear errors for invalid expressions (e.g., `2 ++ 3`).
- Available commands: exit, undo, redo, history, help, clear, clear_history

## Example Usage

```
Welcome to the calculator! Please enter your calculations. Enter 'exit' to quit.
Calculation 1: 2 + 3 * 4
Result: 14
Calculation 2: 8 / 2 + 3
Result: 7
Calculation 3: exit
```