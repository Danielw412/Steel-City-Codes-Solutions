"""Connect 4 solution that checks wins from the last dropped checker."""

import random


ROWS = 6
COLUMNS = 7
EMPTY = "."
PLAYER = "X"
COMPUTER = "O"


def new_board():
    """Create an empty board."""
    return [[EMPTY for _ in range(COLUMNS)] for _ in range(ROWS)]


def print_board(board):
    """Show the board in the terminal."""
    print()
    print("1 2 3 4 5 6 7")

    for row in board:
        print(" ".join(row))

    print()


def valid_columns(board):
    """Find columns that still have room."""
    columns = []

    for column in range(COLUMNS):
        if board[0][column] == EMPTY:
            columns.append(column)

    return columns


def ask_column(board):
    """Ask the player for a valid column."""
    while True:
        answer = input("Choose a column (1-7): ").strip()

        if not answer.isdigit():
            print("Please type a number.")
            continue

        column = int(answer) - 1

        if column not in range(COLUMNS):
            print("That column is outside the board.")
        elif column not in valid_columns(board):
            print("That column is full.")
        else:
            return column


def drop_checker(board, column, symbol):
    """Drop a checker and return the row where it landed."""
    for row in range(ROWS - 1, -1, -1):
        if board[row][column] == EMPTY:
            board[row][column] = symbol
            return row

    return None


def count_direction(board, row, column, row_change, column_change, symbol):
    """Count matching checkers in one direction."""
    count = 0
    row += row_change
    column += column_change

    while 0 <= row < ROWS and 0 <= column < COLUMNS:
        if board[row][column] != symbol:
            break

        count += 1
        row += row_change
        column += column_change

    return count


def won_from_last_move(board, row, column, symbol):
    """Check whether the last move created four in a row."""
    directions = [
        (0, 1),
        (1, 0),
        (1, 1),
        (1, -1),
    ]

    for row_change, column_change in directions:
        total = 1
        total += count_direction(board, row, column, row_change, column_change, symbol)
        total += count_direction(board, row, column, -row_change, -column_change, symbol)

        if total >= 4:
            return True

    return False


def main():
    board = new_board()
    print("Connect 4")
    print("You are X. The computer is O.")

    while True:
        print_board(board)

        player_column = ask_column(board)
        player_row = drop_checker(board, player_column, PLAYER)

        if won_from_last_move(board, player_row, player_column, PLAYER):
            print_board(board)
            print("You win!")
            break

        if len(valid_columns(board)) == 0:
            print_board(board)
            print("Tie game!")
            break

        computer_column = random.choice(valid_columns(board))
        computer_row = drop_checker(board, computer_column, COMPUTER)
        print("Computer chooses column", computer_column + 1)

        if won_from_last_move(board, computer_row, computer_column, COMPUTER):
            print_board(board)
            print("Computer wins.")
            break

        if len(valid_columns(board)) == 0:
            print_board(board)
            print("Tie game!")
            break


if __name__ == "__main__":
    main()
