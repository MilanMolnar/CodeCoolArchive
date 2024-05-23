def word_counter():
    statement = input("Irj be egy mondatot: ")
    x = 1
    for letter in statement:
        if letter == " ":
            x += 1
    print(x)

word_counter()