# Magic 8 Ball: Solutions

Phase 1 (Warm-Up). Student starter code and requirements: [Steel-City-Codes-Starter-Code/phase_1_warm_up/01_magic_8_ball](https://github.com/Danielw412/Steel-City-Codes-Starter-Code/tree/main/phase_1_warm_up/01_magic_8_ball)

These solutions show what a finished project can look like. Students should write their own code. Use these files to answer questions, unblock a stuck student, or check that a project meets the requirements.

## Solution Files

| File | What it demonstrates |
|---|---|
| `solution_1_basic.py` | The whole program in one `while True` loop at the top level, with no functions. The shortest path to a working project. |
| `solution_2_functions.py` | The same game split into small functions (`get_responses`, `wants_to_quit`, `get_answer`) and a `main()`. |
| `solution_3_alternate.py` | Answers grouped by mood in a dictionary, flattened into one list, plus a question counter. |

All three loop until the user quits, skip blank questions, and pick answers with `random.choice()`. They differ in organization, not in behavior.

## What to Look For in Student Code

- A list with at least 9 answers: positive, neutral, and negative.
- `random.choice()` (or `random.randint()` with an index) to pick an answer.
- A loop that keeps asking, and a clear way to quit (`quit`, `q`, `exit`).
- `.strip()` and `.lower()` so extra spaces and capital letters do not break the quit check.
- A check for blank input.
