# Adventure Map: Solutions

Phase 3 (Final Project). Student starter code and requirements: [Steel-City-Codes-Starter-Code/phase_3_final_project/09_adventure_map](https://github.com/Danielw412/Steel-City-Codes-Starter-Code/tree/main/phase_3_final_project/09_adventure_map)

These solutions show what a finished project can look like. Students should write their own code. Use these files to answer questions, unblock a stuck student, or check that a project meets the requirements.

## Solution Files

| File | What it demonstrates |
|---|---|
| `solution_1_grid.py` | A grid of strings with walls (`#`) and a goal (`G`). A direction dictionary maps commands to row and column changes. |
| `solution_2_items.py` | Rooms stored in a dictionary of dictionaries, with exits, items, an inventory, and a locked gate that needs a key. |
| `solution_3_classes.py` | `Room`, `Player`, and `AdventureGame` classes, with a move counter. |

## What to Look For in Student Code

- A map: a grid, or rooms connected by exits.
- Tracking the player's current location.
- Blocked paths and walls that print a message instead of moving the player.
- `.lower()` so `NORTH` works.
- `help` and `quit` commands.
- A goal that ends the game with a win.
