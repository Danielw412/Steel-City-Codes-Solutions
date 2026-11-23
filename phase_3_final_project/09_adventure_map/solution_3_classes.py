"""Adventure Map solution using simple classes."""


class Room:
    """A location in the adventure."""

    def __init__(self, name, description, is_goal=False):
        self.name = name
        self.description = description
        self.is_goal = is_goal
        self.exits = {}

    def connect(self, direction, other_room):
        """Add an exit from this room to another room."""
        self.exits[direction] = other_room


class Player:
    """The player and their current room."""

    def __init__(self, starting_room):
        self.current_room = starting_room
        self.moves = 0

    def move_to(self, room):
        """Move the player to a new room."""
        self.current_room = room
        self.moves += 1


class AdventureGame:
    """A small room-based adventure game."""

    def __init__(self):
        self.rooms = self.build_rooms()
        self.player = Player(self.rooms["porch"])

    def build_rooms(self):
        """Create rooms and connect them."""
        porch = Room("porch", "You stand on a porch outside a strange house.")
        hall = Room("hall", "You are in a long hallway.")
        library = Room("library", "Dusty books cover the walls.")
        garden = Room("garden", "A blocked stone path leads south.")
        attic = Room("attic", "Sunlight shines through a small round window.", True)

        porch.connect("north", hall)
        hall.connect("south", porch)
        hall.connect("east", library)
        hall.connect("west", garden)
        library.connect("west", hall)
        library.connect("north", attic)
        garden.connect("east", hall)

        return {
            "porch": porch,
            "hall": hall,
            "library": library,
            "garden": garden,
            "attic": attic,
        }

    def show_location(self):
        """Print the current room and exits."""
        room = self.player.current_room
        print()
        print(room.description)
        print("Exits:", ", ".join(room.exits.keys()))
        print("Moves:", self.player.moves)

    def move_player(self, command):
        """Try to move in the requested direction."""
        room = self.player.current_room

        if command not in room.exits:
            print("That path is blocked.")
            return

        self.player.move_to(room.exits[command])
        print("You move", command + ".")

    def run(self):
        """Run the adventure until the player wins or quits."""
        print("Adventure Map: House Quest")
        print("Reach the attic. Type help for commands.")

        while True:
            self.show_location()

            if self.player.current_room.is_goal:
                print("You reached the goal in", self.player.moves, "moves!")
                break

            command = input("Command: ").strip().lower()

            if command == "quit":
                print("Goodbye!")
                break
            elif command == "help":
                print("Commands: north, south, east, west, quit")
            else:
                self.move_player(command)


def main():
    game = AdventureGame()
    game.run()


if __name__ == "__main__":
    main()
