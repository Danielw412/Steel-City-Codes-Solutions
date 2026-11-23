# Tic-Tac-Toe: Solutions

Phase 2 (Core Projects). Student starter code and requirements: [Steel-City-Codes-Starter-Code/phase_2_core_projects/05_tic_tac_toe](https://github.com/Danielw412/Steel-City-Codes-Starter-Code/tree/main/phase_2_core_projects/05_tic_tac_toe)

These solutions show what a finished project can look like. Students should write their own code. Use these files to answer questions, unblock a stuck student, or check that a project meets the requirements.

## Solution Files

| File | What it demonstrates |
|---|---|
| `solution_1_basic.py` | A 2D list board, a number-input helper, and a win check written out row by row, column by column, and for both diagonals. |
| `solution_2_functions.py` | `get_lines()` collects every row, column, and diagonal, so the win check is one short loop. Includes `switch_player()`. |
| `solution_3_alternate.py` | A flat list of 9 squares and a list of the 8 winning index triples. `to_index()` converts a row and column to a list position. |

All three are two-player games with a play-again loop.

## What to Look For in Student Code

- A 3 by 3 board as a 2D list (or a flat list, with an explanation).
- Converting the user's 1-3 to a list index 0-2.
- Rejecting numbers outside 1-3 and squares that are already taken.
- Win checks for all 3 rows, 3 columns, and 2 diagonals.
- A tie check when the board is full.
- A play-again loop that starts with a fresh board.
