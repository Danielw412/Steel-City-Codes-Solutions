"""Adventure Map solution using a small grid."""


game_map = [
    ["S", ".", "#", "."],
    [".", ".", "#", "."],
    ["#", ".", ".", "."],
    [".", "#", ".", "G"],
]

directions = {
    "north": (-1, 0),
    "south": (1, 0),
    "east": (0, 1),
    "west": (0, -1),
    "n": (-1, 0),
    "s": (1, 0),
    "e": (0, 1),
    "w": (0, -1),
}


def print_map(player_row, player_column):
    """Print the map with P at the player's location."""
    print()

    for row_index in range(len(game_map)):
        row_display = []

        for column_index in range(len(game_map[row_index])):
            if row_index == player_row and column_index == player_column:
                row_display.append("P")
            else:
                row_display.append(game_map[row_index][column_index])

        print(" ".join(row_display))

    print()
    print("P = player, # = wall, G = goal")


def move_player(player_row, player_column, command):
    """Move the player if the direction is valid and not blocked."""
    if command not in directions:
        print("Unknown command. Type help for commands.")
        return player_row, player_column

    row_change, column_change = directions[command]
    new_row = player_row + row_change
    new_column = player_column + column_change

    if new_row < 0 or new_row >= len(game_map):
        print("You cannot leave the map.")
        return player_row, player_column

    if new_column < 0 or new_column >= len(game_map[0]):
        print("You cannot leave the map.")
        return player_row, player_column

    if game_map[new_row][new_column] == "#":
        print("A wall blocks the way.")
        return player_row, player_column

    print("You move", command + ".")
    return new_row, new_column


def main():
    player_row = 0
    player_column = 0

    print("Adventure Map")
    print("Reach the G. Type help for commands.")

    while True:
        print_map(player_row, player_column)

        if game_map[player_row][player_column] == "G":
            print("You reached the goal!")
            break

        command = input("Command: ").strip().lower()

        if command == "quit":
            print("Goodbye!")
            break

        if command == "help":
            print("Commands: north, south, east, west, quit")
            continue

        player_row, player_column = move_player(player_row, player_column, command)


if __name__ == "__main__":
    main()
