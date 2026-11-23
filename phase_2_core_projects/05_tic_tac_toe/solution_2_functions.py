"""Tic-Tac-Toe solution with reusable board-checking functions."""


def make_board():
    """Return a new board."""
    board = []

    for _ in range(3):
        board.append([" ", " ", " "])

    return board


def show_board(board):
    """Print the current board."""
    print()
    print("Columns: 1   2   3")

    for index, row in enumerate(board):
        print("Row", index + 1, ":", row[0], "|", row[1], "|", row[2])

        if index != 2:
            print("        ---+---+---")

    print()


def ask_for_index(label):
    """Ask for one row or column number and convert it to a list index."""
    while True:
        answer = input(label + " (1-3): ").strip()

        if answer in ["1", "2", "3"]:
            return int(answer) - 1

        print("Please type 1, 2, or 3.")


def ask_for_move(board):
    """Ask until the player chooses an empty square."""
    while True:
        row = ask_for_index("Row")
        column = ask_for_index("Column")

        if board[row][column] == " ":
            return row, column

        print("That spot is already used.")


def get_lines(board):
    """Return all rows, columns, and diagonals."""
    lines = []

    # Rows
    for row in board:
        lines.append(row)

    # Columns
    for column in range(3):
        lines.append([board[0][column], board[1][column], board[2][column]])

    # Diagonals
    lines.append([board[0][0], board[1][1], board[2][2]])
    lines.append([board[0][2], board[1][1], board[2][0]])

    return lines


def has_winner(board, player):
    """Return True if one line contains only the player's symbol."""
    for line in get_lines(board):
        if line == [player, player, player]:
            return True

    return False


def is_tie(board):
    """Return True if the board is full."""
    for row in board:
        if " " in row:
            return False

    return True


def switch_player(player):
    """Return the other player's symbol."""
    if player == "X":
        return "O"

    return "X"


def play_once():
    board = make_board()
    player = "X"

    while True:
        show_board(board)
        print("Player", player, "turn")

        row, column = ask_for_move(board)
        board[row][column] = player

        if has_winner(board, player):
            show_board(board)
            print("Player", player, "wins!")
            return

        if is_tie(board):
            show_board(board)
            print("Tie game!")
            return

        player = switch_player(player)


def main():
    while True:
        play_once()

        answer = input("Play another game? (yes/no): ").strip().lower()
        if answer not in ["yes", "y"]:
            break


if __name__ == "__main__":
    main()
