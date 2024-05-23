def euclidian_algorithm(x, y):  #ref: https://www.youtube.com/watch?v=JUzYl1TYMcU
    r = x%y
    while (r != 0):
        x = y
        y = r
        r = x%y
    return int(y)

while True:
    try:
        x = int(input("Adj meg egy számot: "))
        y = int(input("Adj meg egy másik számot: "))
    except ValueError:
        print("Nem egész számot adott meg!")
        continue
    if isinstance(x, int) and isinstance(y, int):
        break

gcd_result = euclidian_algorithm(x, y)
print(str(x) + " és " + str(y) + " legnagyobb közös osztója: " + str(gcd_result) + "!" )