def pig(widthprompt, lengthprompt):
    while True:
        try:
            width = int(input(widthprompt))
            length = int(input(lengthprompt)) - 2
        except ValueError:
            print("Kerlek szamot adj meg")
            continue
        if isinstance(width, int) and isinstance(length, int):
            break
    star = "*"
    empty_space = " "
    top_bottom_side = width * star
    middle = width - 2
    for i in range(length + 1):
        if i == 0:
            print(top_bottom_side)
        else:
            print(star + (middle * empty_space) + star)
        if i == length:
            print(top_bottom_side)

pig("Add meg a szélességét: ", "Add meg a hosszát: ")