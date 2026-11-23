"""Minesweeper solution that reveals one square at a time."""

import random


HIDDEN = "#"
FLAG = "F"
MINE = "*"

# Each difficulty has a board size and a number of mines.
difficulties = {
    "easy": {"size": 5, "mines": 4},
    "medium": {"size": 7, "mines": 9},
    "hard": {"size": 9, "mines": 16},
}


def choose_difficulty():
    """Ask until the user picks easy, medium, or hard."""
    while True:
        choice = input("Choose a difficulty (easy, medium, hard): ").strip().lower()

        if choice in difficulties:
            return choice

        print("Please type easy, medium, or hard.")


def place_mines(size, mine_count):
    """Return a list of (row, column) spots that hold mines."""
    mines = []

    while len(mines) < mine_count:
        row = random.randint(0, size - 1)
        column = random.randint(0, size - 1)

        if (row, column) not in mines:
            mines.append((row, column))

    return mines


def count_nearby_mines(mines, size, row, column):
    """Count the mines in the 8 squares around one square."""
    count = 0

    for row_change in [-1, 0, 1]:
        for column_change in [-1, 0, 1]:
            next_row = row + row_change
            next_column = column + column_change

            if next_row < 0 or next_row >= size:
                continue

            if next_column < 0 or next_column >= size:
                continue

            if (next_row, next_column) in mines:
                count += 1

    return count


def print_board(view):
    """Print what the player can see, with row and column numbers."""
    size = len(view)
    print()
    print("   " + " ".join(str(number) for number in range(1, size + 1)))

    for row_index in range(size):
        print(str(row_index + 1).rjust(2), " ".join(view[row_index]))

    print()


def get_number(prompt, size):
    """Ask for a row or column number and return it as a list index."""
    while True:
        text = input(prompt).strip()

        if not text.isdigit():
            print("Please enter a number.")
            continue

        number = int(text)

        if number < 1 or number > size:
            print("Please enter a number from 1 to", str(size) + ".")
            continue

        return number - 1


def play_game():
    """Play one game of Minesweeper."""
    difficulty = choose_difficulty()
    size = difficulties[difficulty]["size"]
    mine_count = difficulties[difficulty]["mines"]

    mines = place_mines(size, mine_count)
    view = []

    for _ in range(size):
        view.append([HIDDEN] * size)

    safe_squares_left = size * size - mine_count

    print("There are", mine_count, "mines. Good luck!")

    while True:
        print_board(view)
        action = input("Type r to reveal, f to flag, or q to quit: ").strip().lower()

        if action == "q":
            print("You quit this game.")
            return

        if action not in ["r", "f"]:
            print("Please type r, f, or q.")
            continue

        row = get_number("Row: ", size)
        column = get_number("Column: ", size)
        square = view[row][column]

        if action == "f":
            if square == HIDDEN:
                view[row][column] = FLAG
            elif square == FLAG:
                view[row][column] = HIDDEN
            else:
                print("That square is already revealed.")
            continue

        if square == FLAG:
            print("That square has a flag. Remove the flag first.")
            continue

        if square != HIDDEN:
            print("That square is already revealed.")
            continue

        if (row, column) in mines:
            for mine_row, mine_column in mines:
                view[mine_row][mine_column] = MINE

            print_board(view)
            print("BOOM! You hit a mine. Game over.")
            return

        view[row][column] = str(count_nearby_mines(mines, size, row, column))
        safe_squares_left -= 1

        if safe_squares_left == 0:
            print_board(view)
            print("You cleared every safe square. You win!")
            return


def main():
    print("Minesweeper")
    print("Numbers show how many mines touch that square.")

    while True:
        play_game()

        again = input("Play again? (yes/no): ").strip().lower()
        if again not in ["yes", "y"]:
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()
