# Calculator: Solutions

Phase 1 (Warm-Up). Student starter code and requirements: [Steel-City-Codes-Starter-Code/phase_1_warm_up/03_calculator](https://github.com/Danielw412/Steel-City-Codes-Starter-Code/tree/main/phase_1_warm_up/03_calculator)

These solutions show what a finished project can look like. Students should write their own code. Use these files to answer questions, unblock a stuck student, or check that a project meets the requirements.

## Solution Files

| File | What it demonstrates |
|---|---|
| `solution_1_command_line.py` | A terminal calculator in one loop: two numbers, one operator, `float()` for decimals, `try`/`except ValueError` for bad numbers, and a divide-by-zero check. |
| `solution_2_functions.py` | The same terminal calculator with one function per operation, a `calculate()` function that picks the right one, input functions that ask again on bad input, and `format_number()` so `4.0` prints as `4`. |
| `solution_3_gui.py` | The version the deck asks for: a tkinter window with digit, decimal point, `+ - * /`, `=` and Clear buttons. A `state` dictionary remembers the first number and the operator between clicks. Dividing by zero shows `Error`. |

Solutions 1 and 2 are command-line stepping stones. They are useful for students who need to get the math working before building a window. Solution 3 is the finished project. It opens a window, so run it on a computer with a screen.

## What to Look For in Student Code

- At least `+`, `-`, `*`, and `/`.
- `float()`, not `int()`, so `2.5 + 1` gives `3.5`.
- Dividing by zero shows a message instead of crashing.
- In the window version: each button calls a function (`command=`), and the program remembers the first number and the operator between clicks.
- The `lambda label=label:` trick inside the button loop. Without `label=label`, every button uses the last label in the loop. This is the most common bug in this project.
- The window is created inside `main()`, under `if __name__ == "__main__":`.
