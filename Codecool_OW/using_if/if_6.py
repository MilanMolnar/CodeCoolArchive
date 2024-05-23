def func(prompt):
    statement = input(prompt)
    new_statement = ""
    write = False
    for letter in statement:
        if letter == "<":
            write = True
        if letter == ">":
            write = False
        if write == True:
            new_statement += letter
    for letter in new_statement:
        if letter == "<":
            new_statement = new_statement.replace("<", "\n")
    print(new_statement)

func("Irj be egy mondatot: ")


