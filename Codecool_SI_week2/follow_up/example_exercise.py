def print_if_lower(prompt):
    x = input(prompt)
    if str.islower(x):
        print(x)
    else:
        print("Nem kisbetű!")


print_if_lower("Írj be egy szöveget: ")