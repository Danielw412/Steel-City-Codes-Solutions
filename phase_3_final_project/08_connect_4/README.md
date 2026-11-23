# Connect 4: Solutions

Phase 3 (Final Project). Student starter code and requirements: [Steel-City-Codes-Starter-Code/phase_3_final_project/08_connect_4](https://github.com/Danielw412/Steel-City-Codes-Starter-Code/tree/main/phase_3_final_project/08_connect_4)

These solutions show what a finished project can look like. Students should write their own code. Use these files to answer questions, unblock a stuck student, or check that a project meets the requirements.

## Solution Files

| File | What it demonstrates |
|---|---|
| `solution_1_basic.py` | A 6 by 7 2D list and one `check_direction()` function used for every starting square in 4 directions. |
| `solution_2_functions.py` | Separate functions for horizontal, vertical, and both diagonal checks. Easier to read, but longer. |
| `solution_3_last_move_check.py` | Checks only the lines through the checker that was just dropped, by counting matching checkers in both directions. |

All three play one game against a computer that picks a random open column.

## What to Look For in Student Code

- A 6-row by 7-column board.
- Dropping a checker to the lowest empty row in a column (looping from the bottom up).
- Rejecting column numbers outside 1-7 and full columns.
- Win checks across, up and down, and on both diagonals, without going off the board.
- A tie when every column is full.
- A computer move chosen only from columns that are not full.
