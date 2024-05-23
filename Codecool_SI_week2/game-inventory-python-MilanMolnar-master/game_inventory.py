
# This is the file where you must work.
# Write code in the functions (and create new functions) so that they work
# according to the specification.
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby', 'ruby']
inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
def display_inventory(inventory):
    '''Display the inventory like this:
    rope: 1
    torch: 6
    '''
    for key in inventory:
        print(key + ':', inventory[key])
def add_to_inventory(inventory, added_items):
    '''Add to the inventory dictionary a list of items from added_items.'''
    for loot in added_items:
        if loot not in inventory:
            inventory[loot] = 0

    for key in inventory:
        for loot in added_items:
            if key == loot:
                inventory[key] += 1


def print_table(inventory, order=None):
    '''
    Take your inventory and display it in a well-organized table with
    each column right-justified like this:

    -----------------
    item name | count
    -----------------
         rope |     1
        torch |     6
    -----------------

    The 'order' parameter (string) works as follows:
    - None (by default) means the table is unordered
    - "count,desc" means the table is ordered by count (of items in the
      inventory) in descending order
    - "count,asc" means the table is ordered by count in ascending order
    '''
    if order == None:
        max = 0
        for key in inventory:
            for key2 in inventory:
                if len(key) >= len(key2):
                    if max < len(key):
                        max = len(key)
        if 14 > max:
            maxi = 14
            line = "-" * (maxi + 3)
            print(line + "\n" + " " * (max - 9) + "Item name" + " | count\n" + line)
        else:
            line = "-" * (max + 8)
            print(line + "\n" + " " * (max - 9) + "Item name" + " | count\n" + line)
        for key in inventory:
            print(" " * (max - len(key)) + key + " | " + ' ' * (5 - len(str(inventory[key]))) + str(inventory[key]))
        print(line)
    elif order == "count,asc":
        sorted_list = sorted(inventory.items(), key=lambda item: item[1])
        inventory = dict(sorted_list)
        max = 0
        for key in inventory:
            for key2 in inventory:
                if len(key) >= len(key2):
                    if max < len(key):
                        max = len(key)
        if 14 > max:
            maxi = 14
            line = "-" * (maxi + 3)
            print(line + "\n" + " " * (max - 9) + "Item name" + " | count\n" + line)
        else:
            line = "-" * (max + 8)
            print(line + "\n" + " " * (max - 9) + "Item name" + " | count\n" + line)
        for key in inventory:
            print(" " * (max - len(key)) + key + " | " + ' ' * (5 - len(str(inventory[key]))) + str(inventory[key]))
        print(line)
    elif order == "count,desc":
        sorted_list = sorted(inventory.items(), key=lambda item: item[1], reverse=True)
        inventory = dict(sorted_list)
        max = 0
        for key in inventory:
            for key2 in inventory:
                if len(key) >= len(key2):
                    if max < len(key):
                        max = len(key)
        if 14 > max:
            maxi = 14
            line = "-" * (maxi + 3)
            print(line + "\n" + " " * (max - 9) + "Item name" + " | count\n" + line)
        else:
            line = "-" * (max + 8)
            print(line + "\n" + " " * (max - 9) + "Item name" + " | count\n" + line)
        for key in inventory:
            print(" " * (max - len(key)) + key + " | " + ' ' * (5 - len(str(inventory[key]))) + str(inventory[key]))
        print(line)


def import_inventory(inventory, filename="test_inventory.csv"):
    '''
    Import new inventory items from a file.

    The filename comes as an argument, but by default it's
    "import_inventory.csv". The import automatically merges items by name.

    The file format is plain text with comma separated values (CSV).
    '''
    with open(filename, 'r') as added_file:
        added_items = []
        for line in added_file:
            added_items += line.split(",")
        for loot in added_items:
            if loot not in inventory:
                inventory[loot] = 0
        for key in inventory:
            for loot in added_items:
                if key == loot:
                    inventory[key] += 1


def export_inventory(inventory, filename="export_inventory.csv"):
    '''
    Export the inventory into a .csv file.

    If the filename argument is None, it creates and overwrites a file
    called "export_inventory.csv".

    The file format is plain text with comma separated values (CSV).
    '''
    list_of_items = []
    tuple_of_items = list(inventory.items())
    for tuple in tuple_of_items:
        for j in range(len(tuple)):
            list_of_items.append(tuple[j])
    with open(filename, "w") as file_handler:
        i = 0
        x = 0
        z = 0
        print(list_of_items)
        for f in range(len(list_of_items)):
            if f % 2 != 0:
                z += int(list_of_items[f])
        z -= 1
        while z > x:
            for item in list_of_items:
                if isinstance(item, int):
                    obj = (str(list_of_items[i - 1]) + ",") * item
                    print(item)
                    file_handler.write(obj)
                    x += item
                i += 1

