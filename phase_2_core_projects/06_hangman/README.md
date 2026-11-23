# Hangman: Solutions

Phase 2 (Core Projects). Student starter code and requirements: [Steel-City-Codes-Starter-Code/phase_2_core_projects/06_hangman](https://github.com/Danielw412/Steel-City-Codes-Starter-Code/tree/main/phase_2_core_projects/06_hangman)

These solutions show what a finished project can look like. Students should write their own code. Use these files to answer questions, unblock a stuck student, or check that a project meets the requirements.

## Solution Files

| File | What it demonstrates |
|---|---|
| `solution_1_basic.py` | Everything in nested loops at the top level: build the display, check win or loss, read a guess, update the lists. |
| `solution_2_functions.py` | The same game split into `choose_word()`, `make_display()`, `get_guess()`, and `has_won()`. |
| `solution_3_with_hints.py` | Words stored in a dictionary with a hint for each one. The hint is shown at the start and again after 3 wrong guesses. |

## What to Look For in Student Code

- `random.choice()` to pick a word.
- A display with `_` for letters not yet guessed.
- Validation: exactly one letter, letters only, and no repeated guesses.
- A wrong guess lowers attempts left. A repeated guess does not.
- A win when no `_` remains, and a loss that shows the word.
- A play-again loop.
