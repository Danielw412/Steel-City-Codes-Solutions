"""Adventure Map solution using rooms and a simple item objective."""


rooms = {
    "camp": {
        "description": "You are at a quiet camp.",
        "exits": {"north": "forest", "east": "river"},
        "item": None,
    },
    "forest": {
        "description": "Tall trees surround you.",
        "exits": {"south": "camp", "east": "cave"},
        "item": "map",
    },
    "river": {
        "description": "A river blocks the path east.",
        "exits": {"west": "camp"},
        "item": None,
    },
    "cave": {
        "description": "The cave is cold and dark. A locked gate is north.",
        "exits": {"west": "forest", "north": "tower"},
        "item": "key",
    },
    "tower": {
        "description": "You found the old tower and completed the adventure.",
        "exits": {"south": "cave"},
        "item": None,
    },
}


def show_room(room_name, inventory):
    """Print the current room, exits, items, and inventory."""
    room = rooms[room_name]
    print()
    print(room["description"])
    print("Exits:", ", ".join(room["exits"].keys()))

    if room["item"] is not None:
        print("You see a", room["item"] + ".")

    if len(inventory) == 0:
        print("Inventory: empty")
    else:
        print("Inventory:", ", ".join(inventory))


def take_item(room_name, inventory):
    """Pick up the item in the current room if there is one."""
    item = rooms[room_name]["item"]

    if item is None:
        print("There is nothing to take here.")
        return

    inventory.append(item)
    rooms[room_name]["item"] = None
    print("You picked up the", item + ".")


def move(room_name, command, inventory):
    """Move to another room if the exit exists and is not locked."""
    room = rooms[room_name]

    if command not in room["exits"]:
        print("You cannot go that way.")
        return room_name

    if room_name == "cave" and command == "north" and "key" not in inventory:
        print("The gate is locked. You need a key.")
        return room_name

    return room["exits"][command]


def main():
    current_room = "camp"
    inventory = []

    print("Adventure Map: Key to the Tower")
    print("Commands: north, south, east, west, take, inventory, help, quit")

    while True:
        show_room(current_room, inventory)

        if current_room == "tower":
            print("You win!")
            break

        command = input("Command: ").strip().lower()

        if command == "quit":
            print("Goodbye!")
            break
        elif command == "help":
            print("Try moving with north, south, east, or west.")
            print("Use take to pick up an item.")
        elif command == "inventory":
            print("Inventory:", inventory)
        elif command == "take":
            take_item(current_room, inventory)
        else:
            current_room = move(current_room, command, inventory)


if __name__ == "__main__":
    main()
