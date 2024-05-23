
def remainder(first_num, second_num):
    while True:
        try:
            x = int(input(first_num))
            y = int(input(second_num))
        except ValueError:
            print("Kérlek számot adj meg!")
            continue
        if isinstance(y, int) and isinstance(x, int):
            break
    hanyados = x / y
    maradek = x % y
    print("\nA két szám hányadosa: " + str(hanyados) + "\nA maradék pedig: " + str(maradek) )


remainder("Ird be az első számot: ", "Ird be a második számot: ")
