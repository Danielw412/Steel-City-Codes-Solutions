"""Connect 4 solution using a 2D list and direction checks."""

import random


ROWS = 6
COLUMNS = 7
EMPTY = "."
PLAYER = "X"
COMPUTER = "O"


def create_board():
    """Create an empty Connect 4 board."""
    board = []

    for _ in range(ROWS):
        board.append([EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY])

    return board


def print_board(board):
    """Print the board with column numbers."""
    print()
    print("1 2 3 4 5 6 7")

    for row in board:
        print(" ".join(row))

    print()


def get_valid_columns(board):
    """Return a list of columns that are not full."""
    valid_columns = []

    for column in range(COLUMNS):
        if board[0][column] == EMPTY:
            valid_columns.append(column)

    return valid_columns


def get_player_column(board):
    """Ask the player for a valid column number."""
    while True:
        text = input("Choose a column (1-7): ").strip()

        if not text.isdigit():
            print("Please enter a number.")
            continue

        column = int(text) - 1

        if column < 0 or column >= COLUMNS:
            print("Please choose a column from 1 to 7.")
            continue

        if board[0][column] != EMPTY:
            print("That column is full.")
            continue

        return column


def drop_checker(board, column, symbol):
    """Drop a checker to the lowest open row in a column."""
    for row in range(ROWS - 1, -1, -1):
        if board[row][column] == EMPTY:
            board[row][column] = symbol
            return row

    return None


def check_direction(board, row, column, row_step, column_step, symbol):
    """Check four spaces starting at one location."""
    for step in range(4):
        next_row = row + step * row_step
        next_column = column + step * column_step

        if next_row < 0 or next_row >= ROWS:
            return False

        if next_column < 0 or next_column >= COLUMNS:
            return False

        if board[next_row][next_column] != symbol:
            return False

    return True


def check_winner(board, symbol):
    """Return True if the symbol has four in a row."""
    directions = [
        (0, 1),
        (1, 0),
        (1, 1),
        (1, -1),
    ]

    for row in range(ROWS):
        for column in range(COLUMNS):
            for row_step, column_step in directions:
                if check_direction(board, row, column, row_step, column_step, symbol):
                    return True

    return False


def board_is_full(board):
    """Return True if every column is full."""
    return len(get_valid_columns(board)) == 0


def main():
    board = create_board()

    print("Connect 4")
    print("You are X. The computer is O.")

    while True:
        print_board(board)
        player_column = get_player_column(board)
        drop_checker(board, player_column, PLAYER)

        if check_winner(board, PLAYER):
            print_board(board)
            print("You win!")
            break

        if board_is_full(board):
            print_board(board)
            print("It is a tie!")
            break

        computer_column = random.choice(get_valid_columns(board))
        print("Computer chooses column", computer_column + 1)
        drop_checker(board, computer_column, COMPUTER)

        if check_winner(board, COMPUTER):
            print_board(board)
            print("Computer wins.")
            break

        if board_is_full(board):
            print_board(board)
            print("It is a tie!")
            break


if __name__ == "__main__":
    main()
