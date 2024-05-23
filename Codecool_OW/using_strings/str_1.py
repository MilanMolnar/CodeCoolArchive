def space():
    statement = input("Irj be egy mondatot: ")
    new_statement = ""
    for letter in statement:
        new_statement += letter + " "
    print(new_statement)

space()