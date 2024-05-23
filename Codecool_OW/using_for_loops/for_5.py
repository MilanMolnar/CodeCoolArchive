def pyramid(numprompt):
    while True:
        try:
            z = int(input(numprompt)) + 1
        except ValueError:
            print("Kérlek számot adj meg!")
            continue
        if isinstance(z, int):
            break
    n = 0
    for i in range(z):
        n = i * 2 - 1
        print(" " * (z-1) + n * "*")
        z = z-1

pyramid("Adj meg egy számot:")


