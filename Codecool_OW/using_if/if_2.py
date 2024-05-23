def minus_space():
    statement = input("Irj be egy mondatot: ")
    x = ""
    for letter in statement:
        if letter != " ":
            x += letter
    print(x)

minus_space()