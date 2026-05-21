# ==========================================
# TEXT-BASED INVENTORY GAME
# "Escape the Dungeon"
# ==========================================

# Goal:
# Find the treasure and escape the dungeon.
# You need the Golden Key to unlock the exit.

# -------------------
# INVENTORY SYSTEM
# -------------------

inventory = []
MAX_INVENTORY = 5

# -------------------
# ROOM SYSTEM
# -------------------

rooms = {
    "cell": {
        "description": "A dark prison cell with cold stone walls.",
        "items": [
            {"name": "torch", "type": "tool", "uses": 5},
            {"name": "apple", "type": "food", "uses": 1}
        ],
        "north": "hallway"
    },

    "hallway": {
        "description": "A long hallway with flickering lights.",
        "items": [
            {"name": "medicine", "type": "healing", "uses": 1}
        ],
        "south": "cell",
        "east": "storage",
        "north": "treasure_room"
    },

    "storage": {
        "description": "An old storage room full of dust.",
        "items": [
            {"name": "golden key", "type": "tool", "uses": 1}
        ],
        "west": "hallway"
    },

    "treasure_room": {
        "description": "A room filled with gold and an exit door.",
        "items": [
            {"name": "treasure", "type": "valuable", "uses": 1}
        ],
        "south": "hallway"
    }
}

current_room = "cell"
game_running = True


# -------------------
# HELPER FUNCTIONS
# -------------------

def show_room():
    """Display current room information."""
    room = rooms[current_room]

    print("\n======================")
    print(f"You are in: {current_room.upper()}")
    print(room["description"])
    show_room_items()

    print("\nExits:")
    for direction in ["north", "south", "east", "west"]:
        if direction in room:
            print("-", direction)


def show_room_items():
    """Show items available in the room."""
    room_items = rooms[current_room]["items"]

    if len(room_items) == 0:
        print("\nThere are no items here.")
    else:
        print("\nItems in the room:")
        for item in room_items:
            print("-", item["name"])


def show_inventory():
    """Display player's inventory."""
    print("\n===== INVENTORY =====")

    if len(inventory) == 0:
        print("Your inventory is empty.")
    else:
        for item in inventory:
            print(f"- {item['name']} ({item['type']})")

    print(f"Inventory: {len(inventory)}/{MAX_INVENTORY}")


def pick_up(item_name):
    """Pick up an item from the room."""

    if len(inventory) >= MAX_INVENTORY:
        print("Your inventory is full!")
        return

    room_items = rooms[current_room]["items"]

    for item in room_items:
        if item["name"] == item_name:
            inventory.append(item)
            room_items.remove(item)
            print(f"You picked up the {item_name}.")
            return

    print(f"There is no {item_name} here.")


def drop(item_name):
    """Drop an item into the room."""
    for item in inventory:
        if item["name"] == item_name:
            inventory.remove(item)
            rooms[current_room]["items"].append(item)
            print(f"You dropped the {item_name}.")
            return

    print(f"You don't have a {item_name}.")


def use(item_name):
    """Use an item."""
    global game_running

    for item in inventory:
        if item["name"] == item_name:

            # Food item
            if item["type"] == "food":
                print(f"You eat the {item_name}.")
                inventory.remove(item)

            # Healing item
            elif item["type"] == "healing":
                print(f"You use the {item_name} and feel better.")
                inventory.remove(item)

            # Torch item
            elif item["name"] == "torch":
                item["uses"] -= 1
                print(f"You use the torch. Remaining uses: {item['uses']}")

                if item["uses"] <= 0:
                    print("The torch burned out.")
                    inventory.remove(item)

            # Golden key
            elif item["name"] == "golden key":
                if current_room == "treasure_room":
                    has_treasure = any(i["name"] == "treasure" for i in inventory)
                    if has_treasure:
                        print("\nYou unlock the exit and escape with the treasure!")
                        print("YOU WIN!")
                        game_running = False
                    else:
                        print("You should find the treasure first!")
                else:
                    print("Nothing to unlock here.")

            return

    print(f"You don't have a {item_name}.")


def examine(item_name):
    """Examine an item."""
    # Check inventory first
    for item in inventory:
        if item["name"] == item_name:
            print("\nItem Information:")
            print("Name:", item["name"])
            print("Type:", item["type"])
            print("Uses:", item.get("uses", "N/A"))
            return

    # Check room items
    for item in rooms[current_room]["items"]:
        if item["name"] == item_name:
            print("\nItem Information:")
            print("Name:", item["name"])
            print("Type:", item["type"])
            print("Uses:", item.get("uses", "N/A"))
            return

    print(f"No item named '{item_name}' found.")


def move(direction):
    """Move between rooms."""
    global current_room

    room = rooms[current_room]

    if direction in room:
        current_room = room[direction]
        print(f"You move {direction}.")
        show_room()
    else:
        print("You can't go that way.")


def show_help():
    """Display available commands."""
    print("""
===== COMMANDS =====

move north
move south
move east
move west

inventory
pickup <item>
drop <item>
use <item>
examine <item>

look
help
quit
""")


# -------------------
# GAME LOOP
# -------------------

print("===================================")
print("WELCOME TO ESCAPE THE DUNGEON")
print("===================================")
print("Find the Golden Key and escape!")
show_room()

while game_running:

    command = input("\n> ").lower().strip()

    # Quit
    if command == "quit":
        print("Goodbye!")
        break

    # Help
    elif command == "help":
        show_help()

    # Look around
    elif command == "look":
        show_room()

    # Inventory
    elif command == "inventory":
        show_inventory()

    # Pickup item
    elif command.startswith("pickup "):
        item_name = command[7:]
        pick_up(item_name)

    # Drop item
    elif command.startswith("drop "):
        item_name = command[5:]
        drop(item_name)

    # Use item
    elif command.startswith("use "):
        item_name = command[4:]
        use(item_name)

    # Examine item
    elif command.startswith("examine "):
        item_name = command[8:]
        examine(item_name)

    # Move player
    elif command.startswith("move "):
        direction = command[5:]
        move(direction)

    else:
        print("Unknown command. Type 'help' for commands.")
