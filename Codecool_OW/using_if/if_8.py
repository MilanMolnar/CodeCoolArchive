def min_max(Nprompt, xprompt):
    while True:
        try:
            N = int(input(Nprompt))
        except ValueError:
            print("Kérlek számot adj meg!")
            continue
        if isinstance(N, int):
            break
    min = 9999999999
    max = -999999999
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
        if x > max:
            max = x
    print("minimum: " + str(min))
    print("maximum: " + str(max))


min_max("Ird be mennyi inputot szeretnél: ", "Irj be egy természetes szamot: ")
