"""Minesweeper solution that uses recursion to open empty areas."""

import random


HIDDEN = "#"
FLAG = "F"
MINE = "*"
EMPTY = "."

difficulties = {
    "easy": {"size": 6, "mines": 5},
    "medium": {"size": 8, "mines": 10},
    "hard": {"size": 10, "mines": 18},
}


def choose_difficulty():
    """Ask until the user picks easy, medium, or hard."""
    while True:
        choice = input("Choose a difficulty (easy, medium, hard): ").strip().lower()

        if choice in ["e", "m", "h"]:
            choice = {"e": "easy", "m": "medium", "h": "hard"}[choice]

        if choice in difficulties:
            return choice

        print("Please type easy, medium, or hard.")


def get_neighbors(size, row, column):
    """Return every (row, column) spot that touches this square."""
    neighbors = []

    for row_change in [-1, 0, 1]:
        for column_change in [-1, 0, 1]:
            if row_change == 0 and column_change == 0:
                continue

            next_row = row + row_change
            next_column = column + column_change

            if 0 <= next_row < size and 0 <= next_column < size:
                neighbors.append((next_row, next_column))

    return neighbors


def make_answer_board(size, mine_count):
    """Build the hidden answer: MINE or the number of touching mines."""
    answer = []

    for _ in range(size):
        answer.append([0] * size)

    placed = 0

    while placed < mine_count:
        row = random.randint(0, size - 1)
        column = random.randint(0, size - 1)

        if answer[row][column] != MINE:
            answer[row][column] = MINE
            placed += 1

    for row in range(size):
        for column in range(size):
            if answer[row][column] == MINE:
                continue

            for next_row, next_column in get_neighbors(size, row, column):
                if answer[next_row][next_column] == MINE:
                    answer[row][column] += 1

    return answer


def reveal(answer, view, row, column):
    """Reveal one square. If it touches no mines, reveal its neighbors too.

    This function calls itself, which is called recursion. It stops when it
    reaches a square that is already open, flagged, or next to a mine.
    """
    if view[row][column] != HIDDEN:
        return

    number = answer[row][column]

    if number == 0:
        view[row][column] = EMPTY

        for next_row, next_column in get_neighbors(len(view), row, column):
            reveal(answer, view, next_row, next_column)
    else:
        view[row][column] = str(number)


def count_hidden_safe_squares(answer, view):
    """Count safe squares the player has not opened yet."""
    count = 0

    for row in range(len(view)):
        for column in range(len(view)):
            if answer[row][column] != MINE and view[row][column] in [HIDDEN, FLAG]:
                count += 1

    return count


def show_all_mines(answer, view):
    """Put every mine on the player's view."""
    for row in range(len(view)):
        for column in range(len(view)):
            if answer[row][column] == MINE:
                view[row][column] = MINE


def print_board(view):
    """Print the board with row and column numbers."""
    size = len(view)
    print()
    print("    " + " ".join(str(number).rjust(2) for number in range(1, size + 1)))

    for row_index in range(size):
        squares = " ".join(square.rjust(2) for square in view[row_index])
        print(str(row_index + 1).rjust(2), " " + squares)

    print()


def get_move(size):
    """Ask for a move such as r 2 3 or f 4 1. Return (action, row, column)."""
    while True:
        text = input("Move (r row col, f row col, or q): ").strip().lower()
        parts = text.split()

        if parts == ["q"]:
            return "q", 0, 0

        if len(parts) != 3 or parts[0] not in ["r", "f"]:
            print("Type r 2 3 to reveal row 2, column 3, or f 2 3 to flag it.")
            continue

        if not parts[1].isdigit() or not parts[2].isdigit():
            print("Row and column must be numbers.")
            continue

        row = int(parts[1]) - 1
        column = int(parts[2]) - 1

        if row < 0 or row >= size or column < 0 or column >= size:
            print("Row and column must be from 1 to", str(size) + ".")
            continue

        return parts[0], row, column


def play_game():
    """Play one game. Return True for a win and False otherwise."""
    difficulty = choose_difficulty()
    size = difficulties[difficulty]["size"]
    mine_count = difficulties[difficulty]["mines"]

    answer = make_answer_board(size, mine_count)
    view = [[HIDDEN] * size for _ in range(size)]

    print("Mines hidden:", mine_count)

    while True:
        print_board(view)
        action, row, column = get_move(size)

        if action == "q":
            print("You quit this game.")
            return False

        if action == "f":
            if view[row][column] == HIDDEN:
                view[row][column] = FLAG
            elif view[row][column] == FLAG:
                view[row][column] = HIDDEN
            else:
                print("You can only flag a hidden square.")
            continue

        if view[row][column] == FLAG:
            print("Remove the flag before revealing that square.")
            continue

        if answer[row][column] == MINE:
            show_all_mines(answer, view)
            print_board(view)
            print("BOOM! You hit a mine. Game over.")
            return False

        reveal(answer, view, row, column)

        if count_hidden_safe_squares(answer, view) == 0:
            print_board(view)
            print("You cleared the board. You win!")
            return True


def main():
    print("Minesweeper")
    print("Reveal every square that does not hide a mine.")
    wins = 0
    games = 0

    while True:
        if play_game():
            wins += 1

        games += 1
        print("You have won", wins, "of", games, "game(s).")

        again = input("Play again? (yes/no): ").strip().lower()
        if again not in ["yes", "y"]:
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()
