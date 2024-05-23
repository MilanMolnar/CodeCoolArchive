
def mini_mtable(num):
    while True:
        try:
            x = float(input(num))
        except ValueError:
            print("Kérem szamot adjon meg!")
            continue
        if isinstance(x, float):
            break
    list = [""]
    for i in range(1,6):
        list.append(x * i)

    print(str(x) + " szorozva 1-el: " + str(list[1]))
    print(str(x) + " szorozva 2-vel: " + str(list[2]))
    print(str(x) + " szorozva 3-mal: " + str(list[3]))
    print(str(x) + " szorozva 4-gyel: " + str(list[4]))
    print(str(x) + " szorozva 5-tel: " + str(list[5]))


mini_mtable("Add meg a szamot a kis szorzótábla létrehozásához!\nSzám: ")