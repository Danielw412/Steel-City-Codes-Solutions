"""The list of projects shown in the arcade.

solution_1_arcade.py imports this file. Keeping the data here and the window
code in another file shows how one Python file can import another.

Each project is a dictionary. The "script" path starts at the top folder of
this repository, so the arcade can find it from anywhere.
"""


projects = [
    {
        "name": "Magic 8 Ball",
        "creator": "Instructor example",
        "script": "phase_1_warm_up/01_magic_8_ball/solution_2_functions.py",
        "instructions": (
            "Ask a yes-or-no question and the Magic 8 Ball gives a random answer.\n"
            "Type quit when you are done."
        ),
    },
    {
        "name": "Rock Paper Scissors",
        "creator": "Instructor example",
        "script": "phase_1_warm_up/02_rock_paper_scissors/solution_3_alternate.py",
        "instructions": (
            "Type rock, paper, or scissors (or r, p, s) to play against the computer.\n"
            "Rock beats scissors, scissors beats paper, and paper beats rock."
        ),
    },
    {
        "name": "Calculator",
        "creator": "Instructor example",
        "script": "phase_1_warm_up/03_calculator/solution_3_gui.py",
        "instructions": (
            "Click numbers and an operator (+, -, *, /), then click = to see the answer.\n"
            "This project opens its own window. Close it to come back to the arcade."
        ),
    },
    {
        "name": "Chatbot",
        "creator": "Instructor example",
        "script": "phase_2_core_projects/04_chatbot/solution_3_dictionary.py",
        "instructions": (
            "Chat with the bot. It knows about python, bears, music, and weather.\n"
            "Type bye to leave."
        ),
    },
    {
        "name": "Tic-Tac-Toe",
        "creator": "Instructor example",
        "script": "phase_2_core_projects/05_tic_tac_toe/solution_1_basic.py",
        "instructions": (
            "Two players take turns as X and O.\n"
            "Type a row and a column from 1 to 3. Get three in a row to win."
        ),
    },
    {
        "name": "Hangman",
        "creator": "Instructor example",
        "script": "phase_2_core_projects/06_hangman/solution_3_with_hints.py",
        "instructions": (
            "Guess the secret word one letter at a time.\n"
            "Six wrong guesses and the game is over."
        ),
    },
    {
        "name": "Minesweeper",
        "creator": "Instructor example",
        "script": "phase_3_final_project/07_minesweeper/solution_2_flood_fill.py",
        "instructions": (
            "Open every square that does not hide a mine.\n"
            "Type r 2 3 to reveal row 2, column 3, or f 2 3 to put a flag there."
        ),
    },
    {
        "name": "Connect 4",
        "creator": "Instructor example",
        "script": "phase_3_final_project/08_connect_4/solution_1_basic.py",
        "instructions": (
            "Drop checkers into a column from 1 to 7.\n"
            "Get four in a row across, up and down, or diagonally before the computer."
        ),
    },
    {
        "name": "Adventure Map",
        "creator": "Instructor example",
        "script": "phase_3_final_project/09_adventure_map/solution_2_items.py",
        "instructions": (
            "Explore with north, south, east, and west. Type take to pick up items.\n"
            "Find the key and reach the tower."
        ),
    },
]
