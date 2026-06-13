"""Tic-Tac-Toe solution using a flat list for the board."""


winning_lines = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6],
]


def new_board():
    """Return a flat board with 9 spaces."""
    return [" ", " ", " ", " ", " ", " ", " ", " ", " "]


def to_index(row, column):
    """Convert a row and column into a flat-list index."""
    return row * 3 + column


def print_board(board):
    """Print a flat-list board as three rows."""
    print()
    print("    1   2   3")

    for row in range(3):
        first = to_index(row, 0)
        print(row + 1, " ", board[first], "|", board[first + 1], "|", board[first + 2])

        if row < 2:
            print("   ---+---+---")

    print()


def read_row_or_column(prompt):
    """Read a row or column from the user."""
    while True:
        text = input(prompt).strip()

        if text in ["1", "2", "3"]:
            return int(text) - 1

        print("Enter 1, 2, or 3.")


def get_move(board):
    """Ask for row and column, then return a flat-list index."""
    while True:
        row = read_row_or_column("Row (1-3): ")
        column = read_row_or_column("Column (1-3): ")
        index = to_index(row, column)

        if board[index] == " ":
            return index

        print("That square is taken.")


def winner_exists(board, player):
    """Return True when the player controls any winning line."""
    for line in winning_lines:
        first, second, third = line

        if board[first] == player and board[second] == player and board[third] == player:
            return True

    return False


def play_game():
    board = new_board()
    player = "X"

    while True:
        print_board(board)
        print("Player", player)
        index = get_move(board)
        board[index] = player

        if winner_exists(board, player):
            print_board(board)
            print("Player", player, "wins!")
            return

        if " " not in board:
            print_board(board)
            print("Tie game!")
            return

        player = "O" if player == "X" else "X"


def main():
    while True:
        play_game()

        again = input("Play again? (yes/no): ").strip().lower()
        if again not in ["yes", "y"]:
            print("Goodbye!")
            return


if __name__ == "__main__":
    main()
