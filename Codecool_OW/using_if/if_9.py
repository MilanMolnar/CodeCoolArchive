def pitagoras(ap, bp, cp):
    while True:
        try:
            a = float(input(ap))
            b = float(input(bp))
            c = float(input(cp))
        except ValueError:
            print("Kérlek számot adj meg!")
            continue
        if isinstance(a, float) and isinstance(b, float) and isinstance(c, float):
            break
    if (a**2 + b**2) == (c**2):
        print("Lehetséges!")
    else:
        print("Nem lehetséges")

pitagoras("Add meg az \"a\" oldal hosszát: ", "Add meg az \"b\" oldal hosszát: ", "Add meg az \"c\" oldal hosszát: ")