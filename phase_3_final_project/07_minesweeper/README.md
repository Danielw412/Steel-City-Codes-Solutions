# Minesweeper: Solutions

Phase 3 (Final Project). Student starter code and requirements: [Steel-City-Codes-Starter-Code/phase_3_final_project/07_minesweeper](https://github.com/Danielw412/Steel-City-Codes-Starter-Code/tree/main/phase_3_final_project/07_minesweeper)

These solutions show what a finished project can look like. Students should write their own code. Use these files to answer questions, unblock a stuck student, or check that a project meets the requirements.

## Solution Files

| File | What it demonstrates |
|---|---|
| `solution_1_basic.py` | Functions and a list of mine positions. The player picks a difficulty, then types `r` or `f` and a row and a column at separate prompts. Revealing opens one square only, with no recursion. A stepping stone, not the finished project. |
| `solution_2_flood_fill.py` | The finished project the deck asks for. A hidden answer board stores `*` or the count of touching mines. `reveal()` calls itself on every neighbor when a square touches 0 mines, so empty areas open automatically. Moves are typed in one line, such as `r 2 3` or `f 2 3`. Tracks wins across games. |
| `solution_3_classes.py` | The same game with `Square`, `Board`, and `MinesweeperGame` classes. `Board.reveal()` uses the same recursion. Mines are placed after the first reveal, so the first square is always safe. Tracks wins and losses. |

All three have easy, medium, and hard difficulties, flags that can be placed and removed, game over on a mine (showing every mine), a win when all safe squares are open, and a play-again loop.

The deck's version of this project uses Pygame. These solutions are command-line versions to match the other projects. A Pygame window is an optional add-on: it needs `pip install pygame`.

## What to Look For in Student Code

- A 2D list for the board, and a separate view of what the player can see (or a class that tracks both).
- Counting the 8 neighbors without going off the edge of the board.
- Input validation for the difficulty, the command, and the row and column.
- Flags that block revealing until removed.
- Recursion in `reveal()`. Check for the stopping cases: an already-open square, a flagged square, and a square next to a mine. A missing "already open" check makes the function call itself forever and crash with `RecursionError`.
- Win detection that counts safe squares, not flags.
