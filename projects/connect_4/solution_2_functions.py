"""Connect 4 solution with separate win-checking functions."""

import random


ROWS = 6
COLUMNS = 7
EMPTY = "."
PLAYER = "X"
COMPUTER = "O"


def make_board():
    """Return a new empty board."""
    return [[EMPTY for _ in range(COLUMNS)] for _ in range(ROWS)]


def show_board(board):
    """Display the board."""
    print()
    print(" ".join(str(number) for number in range(1, COLUMNS + 1)))

    for row in board:
        print(" ".join(row))

    print()


def column_is_open(board, column):
    """Return True when a checker can be dropped in the column."""
    return board[0][column] == EMPTY


def open_columns(board):
    """Return all columns that are still open."""
    columns = []

    for column in range(COLUMNS):
        if column_is_open(board, column):
            columns.append(column)

    return columns


def ask_player_column(board):
    """Read and validate the player's column choice."""
    while True:
        answer = input("Column (1-7): ").strip()

        if not answer.isdigit():
            print("Numbers only, please.")
            continue

        column = int(answer) - 1

        if column < 0 or column >= COLUMNS:
            print("Choose a column from 1 to 7.")
        elif not column_is_open(board, column):
            print("That column is full.")
        else:
            return column


def drop(board, column, symbol):
    """Place the symbol in the lowest open row."""
    for row in range(ROWS - 1, -1, -1):
        if board[row][column] == EMPTY:
            board[row][column] = symbol
            return


def check_horizontal(board, symbol):
    """Check for four across."""
    for row in range(ROWS):
        count = 0

        for column in range(COLUMNS):
            if board[row][column] == symbol:
                count += 1
            else:
                count = 0

            if count == 4:
                return True

    return False


def check_vertical(board, symbol):
    """Check for four up and down."""
    for column in range(COLUMNS):
        count = 0

        for row in range(ROWS):
            if board[row][column] == symbol:
                count += 1
            else:
                count = 0

            if count == 4:
                return True

    return False


def check_down_diagonal(board, symbol):
    """Check diagonals that go down and right."""
    for row in range(ROWS - 3):
        for column in range(COLUMNS - 3):
            if board[row][column] == symbol:
                if board[row + 1][column + 1] == symbol:
                    if board[row + 2][column + 2] == symbol:
                        if board[row + 3][column + 3] == symbol:
                            return True

    return False


def check_up_diagonal(board, symbol):
    """Check diagonals that go up and right."""
    for row in range(3, ROWS):
        for column in range(COLUMNS - 3):
            if board[row][column] == symbol:
                if board[row - 1][column + 1] == symbol:
                    if board[row - 2][column + 2] == symbol:
                        if board[row - 3][column + 3] == symbol:
                            return True

    return False


def has_winner(board, symbol):
    """Return True if the symbol has won."""
    return (
        check_horizontal(board, symbol)
        or check_vertical(board, symbol)
        or check_down_diagonal(board, symbol)
        or check_up_diagonal(board, symbol)
    )


def play_game():
    board = make_board()

    while True:
        show_board(board)
        player_column = ask_player_column(board)
        drop(board, player_column, PLAYER)

        if has_winner(board, PLAYER):
            show_board(board)
            print("You win!")
            return

        if len(open_columns(board)) == 0:
            show_board(board)
            print("Tie game!")
            return

        computer_column = random.choice(open_columns(board))
        print("Computer chooses", computer_column + 1)
        drop(board, computer_column, COMPUTER)

        if has_winner(board, COMPUTER):
            show_board(board)
            print("Computer wins.")
            return

        if len(open_columns(board)) == 0:
            show_board(board)
            print("Tie game!")
            return


def main():
    print("Connect 4")
    play_game()


if __name__ == "__main__":
    main()
