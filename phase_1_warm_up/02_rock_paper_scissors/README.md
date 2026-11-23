# Rock Paper Scissors: Solutions

Phase 1 (Warm-Up). Student starter code and requirements: [Steel-City-Codes-Starter-Code/phase_1_warm_up/02_rock_paper_scissors](https://github.com/Danielw412/Steel-City-Codes-Starter-Code/tree/main/phase_1_warm_up/02_rock_paper_scissors)

These solutions show what a finished project can look like. Students should write their own code. Use these files to answer questions, unblock a stuck student, or check that a project meets the requirements.

## Solution Files

| File | What it demonstrates |
|---|---|
| `solution_1_basic.py` | Exactly 3 rounds with a `for` loop, an input-validation loop, and an `if`/`elif` chain for every winning case. Prints a final score. |
| `solution_2_functions.py` | Functions for the user's choice, the computer's choice, and the result. Plays until the user says no. |
| `solution_3_alternate.py` | A `beats` dictionary replaces the long `if`/`elif` chain, `r`/`p`/`s` shortcuts, and a score dictionary. |

## What to Look For in Student Code

- Input validation: an invalid choice such as `banana` asks again instead of crashing.
- `.lower()` so `ROCK` works.
- The tie case checked first, then the three winning combinations, then "lose".
- A loop for at least 3 rounds or a play-again question.
- Score tracking, if the student tried the add-on.
