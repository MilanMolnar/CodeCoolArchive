def min(Nprompt, xprompt):
    while True:
        try:
            N = int(input(Nprompt))
        except ValueError:
            print("Kérlek számot adj meg!")
            continue
        if isinstance(N, int):
            break
    min = 9999999999
    for i in range(N):
        while True:
            try:
                x = int(input(xprompt))
            except ValueError:
                print("Kérlek számot adj meg!")
                continue
            if isinstance(x, int):
                break
        if x < min:
            min = x
    print("Az inputok minimum értéke: " + str(min))

min("Ird be mennyi számot szeretnél tesztelni: ", "Irj be egy egész számot: ")