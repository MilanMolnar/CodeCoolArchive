def greedy(amountprompt):
    while True:
        try:
            amount = int(input(amountprompt))
        except ValueError:
            print("Nem számot adtal meg!")
            continue
        if isinstance(amount, int):
            break
    coins = [10, 5, 2, 1]
    print("Felhasznált érmék: ", end = "")
    iterations = 0
    for i in range(len(coins)):
        while amount >= coins[i]:
            amount = amount - coins[i]
            iterations += 1
            print(str(coins[i]) + " ", end = '' )
    print("\n\nÖsszesen: " + str(iterations) + " érmére van szükség!")


greedy("Ird be az értéket: ")