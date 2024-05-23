def calc(xprompt, yprompt):
    while True:
        try:
            x = int(input(xprompt))
        except ValueError:
            print("Kérlek számot adj meg!")
            continue
        if isinstance(x, int):
            break
    even = 0
    odd = 0
    odd_total = 0
    for i in range(x):
        while True:
            try:
                y = int(input(yprompt))
            except ValueError:
                print("Kérlek számot adj meg!")
                continue
            if isinstance(y, int):
                break
        if y % 2 == 0:
            even += 1
        else:
            odd += 1
            odd_total += y

    print("\nPáros szám: " + str(even) + "\nPáratlan: " + str(odd) + "\nPáratlan összes: " + str(odd_total))
calc("Mennyi számot szeretne tesztelni?: ","ird be a tesztelni kivant szamot: " )