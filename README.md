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
pytest --cov=app --cov-report=term-missing --cov-fail-under=90 -v
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


- Supports addition, subtraction, multiplication, division, power, root, modulus, integer division, percent, and absolute difference operations.
- Handles operator precedence (PEMDAS).
- Returns integer results when possible, otherwise float.
- Logs calculation steps and errors for easier debugging (to `logs/calculator.log`).
- Raises clear errors for invalid expressions (e.g., `2 ++ 3`).
- Available commands: exit, undo, redo, history, help, clear, clear_history
- Expression parser supports multi-operator and multi-digit expressions (e.g., `2 + 3 * 4 - 5 / 2`).
- Custom exceptions for operation and validation errors.
- Logging to file for all calculation steps and errors.
- History is persisted to CSV and supports undo/redo/clear/history commands.
- Environment variable support for history file location.
- Modular code structure (separate calculation, operation, memento, and exception modules).
- Parameterized and comprehensive tests for all operations and expression parsing.
- Test coverage enforcement (90%+) using pytest and pytest-cov.
- Skipped or excluded tests do not affect coverage metrics.
- Easy extensibility for new operations or features.

## Example Usage

```
Welcome to the calculator! Please enter your calculations. Enter 'exit' to quit.
Calculation 1: 2 + 3 * 4
Result: 14
Calculation 2: 8 / 2 + 3
Result: 7
Calculation 3: exit
```