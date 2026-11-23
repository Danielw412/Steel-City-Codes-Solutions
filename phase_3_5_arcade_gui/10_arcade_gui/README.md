# Arcade GUI: Solutions

Phase 3.5 (optional). Student starter code and requirements: [Steel-City-Codes-Starter-Code/phase_3_5_arcade_gui/10_arcade_gui](https://github.com/Danielw412/Steel-City-Codes-Starter-Code/tree/main/phase_3_5_arcade_gui/10_arcade_gui)

These solutions show what a finished project can look like. Students should write their own code. Use these files to answer questions, unblock a stuck student, or check that a project meets the requirements.

## Solution Files

| File | What it demonstrates |
|---|---|
| `solution_1_arcade.py` | A tkinter `ArcadeApp` class with a welcome page, a menu page with one button per project, and a page per project with its instructions, the creator's name, and a Launch button. Launch runs the project with `subprocess.run([sys.executable, script])`, so it uses the same Python and the terminal the arcade was started from. The arcade window hides while the game runs and comes back when it ends. A missing file shows an error message. |
| `arcade_projects.py` | The list of projects, one dictionary each. `solution_1_arcade.py` imports it, which shows how one Python file imports another. |

The project paths in `arcade_projects.py` point at other solutions in this repository, relative to the repository's top folder, so you can demo the arcade straight away. In a real class, each entry points at a student's finished project and names that student as the creator.

Run it from any folder with `python solution_1_arcade.py`. It opens a window, so run it on a computer with a screen.

## What to Look For in Student Code

- A list of dictionaries for the projects (the deck lists dictionaries, classes, and importing).
- A class for the app, with one method per page.
- Clearing the old page before drawing the next one.
- The `lambda project=project:` trick in the menu loop. Without `project=project`, every button opens the last project.
- `sys.executable` instead of a hard-coded `python`, so the same Python runs the games.
- File paths built from `__file__`, so the arcade works no matter which folder it is started from.
- The window is created inside `main()`, under `if __name__ == "__main__":`.
