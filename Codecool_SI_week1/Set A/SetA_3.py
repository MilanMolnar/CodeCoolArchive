def variation0():
    list_of_fibonacci = []
    n = 30
    it = 0
    for i in range(n):
        while it < 2:
            list_of_fibonacci.append(1)
            it += 1
            if it >= 2:
                break
        y = list_of_fibonacci[i] + list_of_fibonacci[i + 1]
        list_of_fibonacci.append(y)
        print(list_of_fibonacci[i])

def variation1(parameter):
    list_of_fibonacci = []
    while True:
        try:
            n = int(input(parameter))
        except ValueError:
            print("Nem számot adott meg!")
            continue
        if isinstance(n, int):
            break
    it = 0
    for i in range(n):
        while it < 2:
            list_of_fibonacci.append(1)
            it += 1
            if it >= 2:
                break
        y = list_of_fibonacci[i] + list_of_fibonacci[i + 1]
        list_of_fibonacci.append(y)
        print(list_of_fibonacci[i])

def variation2(parameter2):
    list_of_fibonacci = []
    while True:
        try:
            n = int(input(parameter2))
        except ValueError:
            print("Nem számot adott meg!")
            continue
        if isinstance(n, int):
            break
    it = 0
    for i in range(n):
        while it < 2:
            list_of_fibonacci.append(1)
            it += 1
            if it >= 2:
                break
        y = list_of_fibonacci[i] + list_of_fibonacci[i + 1]
        list_of_fibonacci.append(y)
        l = len(str(list_of_fibonacci[i]))
        print(str(i + 1) + ".", end="")
        if i + 1 < 10:
            print(" " * (20 - l), end="")
        elif i + 1 < 100:
            print(" " * (19 - l), end="")
        else:
            print(" " * (18 - l), end="")
        print(list_of_fibonacci[i])

print("Irja be, hogy hanyadik variációt szeretné látni a Set A_3-ik feladatból [0, 1, 2]", end="")
while True:
    set = input(": ")
    if set in ["0","1","2"]:
        if set == "0":
            variation0()
            break
        elif set == "1":
            variation1("Add meg a hosszát a fibonacci listának!\n: ")
            break
        elif set == "2":
            variation2("Add meg a hosszát a fibonacci listának!\n: ")
            break
    else:
        print("A variációk száma [0, 1, 2]")
        continue

