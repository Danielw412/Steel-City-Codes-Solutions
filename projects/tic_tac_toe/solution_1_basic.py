"""Two-player Tic-Tac-Toe solution using a 2D list."""


def create_board():
    """Create an empty 3 by 3 board."""
    return [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]


def print_board(board):
    """Print the board with row and column numbers."""
    print()
    print("    1   2   3")

    for row_number in range(3):
        row = board[row_number]
        print(row_number + 1, " ", row[0], "|", row[1], "|", row[2])

        if row_number < 2:
            print("   ---+---+---")

    print()


def get_number(prompt):
    """Ask for a number from 1 to 3."""
    while True:
        text = input(prompt).strip()

        if not text.isdigit():
            print("Please enter a number.")
            continue

        number = int(text)

        if number < 1 or number > 3:
            print("Please enter 1, 2, or 3.")
            continue

        return number - 1


def get_move(board, player):
    """Ask the current player for a valid open square."""
    while True:
        print("Player", player, "turn")
        row = get_number("Row (1-3): ")
        column = get_number("Column (1-3): ")

        if board[row][column] == " ":
            return row, column

        print("That square is already taken.")


def check_winner(board, player):
    """Return True if the player has three in a row."""
    for row in board:
        if row[0] == player and row[1] == player and row[2] == player:
            return True

    for column in range(3):
        if board[0][column] == player and board[1][column] == player and board[2][column] == player:
            return True

    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True

    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True

    return False


def board_is_full(board):
    """Return True if no empty squares remain."""
    for row in board:
        for square in row:
            if square == " ":
                return False

    return True


def play_game():
    """Play one full game."""
    board = create_board()
    current_player = "X"

    while True:
        print_board(board)
        row, column = get_move(board, current_player)
        board[row][column] = current_player

        if check_winner(board, current_player):
            print_board(board)
            print("Player", current_player, "wins!")
            break

        if board_is_full(board):
            print_board(board)
            print("It is a tie!")
            break

        if current_player == "X":
            current_player = "O"
        else:
            current_player = "X"


def main():
    print("Tic-Tac-Toe")

    while True:
        play_game()
        again = input("Play again? (yes/no): ").strip().lower()

        if again not in ["yes", "y"]:
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()
