
def greedy(amountprompt):                   #Variable 6, greedy algorithm.
    while True:
        try:
            amount = int(input(amountprompt))
        except ValueError:
            print("Nem számot adtal meg!")
            continue
        if isinstance(amount, int):
            break
    arab_num = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    iterations = 0
    roman_coin = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    for i in range(len(arab_num)):
        while amount >= arab_num[i]:
            amount = amount - arab_num[i]
            iterations += 1
            print(str(roman_coin[i]), end='')

greedy("Ird be az értéket: ")