"""Minesweeper solution using classes for the squares, the board, and the game."""

import random


difficulties = {
    "easy": {"size": 6, "mines": 5},
    "medium": {"size": 8, "mines": 10},
    "hard": {"size": 10, "mines": 18},
}


class Square:
    """One square on the board."""

    def __init__(self):
        self.has_mine = False
        self.is_revealed = False
        self.is_flagged = False
        self.nearby_mines = 0

    def symbol(self, show_mines=False):
        """Return the character to print for this square."""
        if self.has_mine and (self.is_revealed or show_mines):
            return "*"

        if self.is_flagged:
            return "F"

        if not self.is_revealed:
            return "#"

        if self.nearby_mines == 0:
            return "."

        return str(self.nearby_mines)


class Board:
    """A square grid of Square objects."""

    def __init__(self, size, mine_count):
        self.size = size
        self.mine_count = mine_count
        self.mines_placed = False
        self.squares = [[Square() for _ in range(size)] for _ in range(size)]

    def neighbors(self, row, column):
        """Return the (row, column) spots that touch this square."""
        spots = []

        for row_change in [-1, 0, 1]:
            for column_change in [-1, 0, 1]:
                next_row = row + row_change
                next_column = column + column_change

                if (row_change, column_change) == (0, 0):
                    continue

                if 0 <= next_row < self.size and 0 <= next_column < self.size:
                    spots.append((next_row, next_column))

        return spots

    def place_mines(self, safe_row, safe_column):
        """Place mines anywhere except the first square the player opens."""
        open_spots = []

        for row in range(self.size):
            for column in range(self.size):
                if (row, column) != (safe_row, safe_column):
                    open_spots.append((row, column))

        for row, column in random.sample(open_spots, self.mine_count):
            self.squares[row][column].has_mine = True

        for row in range(self.size):
            for column in range(self.size):
                for next_row, next_column in self.neighbors(row, column):
                    if self.squares[next_row][next_column].has_mine:
                        self.squares[row][column].nearby_mines += 1

        self.mines_placed = True

    def toggle_flag(self, row, column):
        """Add or remove a flag. Return a message for the player."""
        square = self.squares[row][column]

        if square.is_revealed:
            return "That square is already open."

        square.is_flagged = not square.is_flagged

        if square.is_flagged:
            return "Flag placed."

        return "Flag removed."

    def reveal(self, row, column):
        """Open a square, using recursion to open empty areas.

        Return True if the square had a mine.
        """
        if not self.mines_placed:
            self.place_mines(row, column)

        square = self.squares[row][column]

        if square.is_revealed or square.is_flagged:
            return False

        square.is_revealed = True

        if square.has_mine:
            return True

        if square.nearby_mines == 0:
            for next_row, next_column in self.neighbors(row, column):
                self.reveal(next_row, next_column)

        return False

    def all_safe_squares_open(self):
        """Return True when every square without a mine is revealed."""
        for row in self.squares:
            for square in row:
                if not square.has_mine and not square.is_revealed:
                    return False

        return True

    def show(self, show_mines=False):
        """Print the board with row and column numbers."""
        print()
        print("    " + " ".join(str(number).rjust(2) for number in range(1, self.size + 1)))

        for row_index, row in enumerate(self.squares):
            symbols = " ".join(square.symbol(show_mines).rjust(2) for square in row)
            print(str(row_index + 1).rjust(2), " " + symbols)

        print()


class MinesweeperGame:
    """Runs games, asks for moves, and keeps score."""

    def __init__(self):
        self.wins = 0
        self.losses = 0

    def choose_difficulty(self):
        """Ask until the user picks a difficulty."""
        while True:
            choice = input("Choose a difficulty (easy, medium, hard): ").strip().lower()

            if choice in difficulties:
                return difficulties[choice]

            print("Please type easy, medium, or hard.")

    def ask_move(self, size):
        """Ask for a move such as r 2 3. Return (action, row, column)."""
        while True:
            parts = input("Move (r row col, f row col, or q): ").strip().lower().split()

            if parts == ["q"]:
                return "q", 0, 0

            if len(parts) == 3 and parts[0] in ["r", "f"]:
                if parts[1].isdigit() and parts[2].isdigit():
                    row = int(parts[1]) - 1
                    column = int(parts[2]) - 1

                    if 0 <= row < size and 0 <= column < size:
                        return parts[0], row, column

            print("Example moves: r 2 3 reveals row 2, column 3. f 2 3 flags it.")

    def play_one_game(self):
        """Play until the player wins, loses, or quits."""
        settings = self.choose_difficulty()
        board = Board(settings["size"], settings["mines"])
        print("Mines hidden:", board.mine_count, "- your first square is always safe.")

        while True:
            board.show()
            action, row, column = self.ask_move(board.size)

            if action == "q":
                print("You quit this game.")
                return

            if action == "f":
                print(board.toggle_flag(row, column))
                continue

            if board.squares[row][column].is_flagged:
                print("Remove the flag before revealing that square.")
                continue

            if board.reveal(row, column):
                board.show(show_mines=True)
                print("BOOM! You hit a mine. Game over.")
                self.losses += 1
                return

            if board.all_safe_squares_open():
                board.show(show_mines=True)
                print("You cleared the board. You win!")
                self.wins += 1
                return

    def run(self):
        """Keep playing games until the player is done."""
        print("Minesweeper")

        while True:
            self.play_one_game()
            print("Wins:", self.wins, " Losses:", self.losses)

            again = input("Play again? (yes/no): ").strip().lower()
            if again not in ["yes", "y"]:
                print("Thanks for playing!")
                break


def main():
    game = MinesweeperGame()
    game.run()


if __name__ == "__main__":
    main()
