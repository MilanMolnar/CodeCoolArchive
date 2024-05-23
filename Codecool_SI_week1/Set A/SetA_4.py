import random


def risk():
    atk_lost = 0
    def_lost = 0
    it2 = 0
    it = 0
    atk = ""
    defe = ""
    al = []
    dl = []
    list_of_roll = []

    while True:                                                             #Tesztelés attackerek száma inputra
        try:
            inp_atk = int(input("ird be az attackerek számát: "))
        except ValueError:
            print("Nem számot adtál meg!")
            continue
        if inp_atk in [1, 2, 3]:
            break
        else:
            print("A deffenderek száma csak 1, 2 és 3 lehet!")
            continue

    while True:                                                             #Tesztelés defenderek száma inputra
        try:
            inp_def = int(input("ird be az defenderek számát: "))
        except ValueError:
            print("Nem számot adtál meg!")
            continue
        if inp_def in [1, 2]:
            break
        else:
            print("A deffenderek száma csak 1 és 2 lehet!")
            continue

    for i in range(inp_atk + inp_def):                                      #Két input összege a range
        list.append(list_of_roll, random.randrange(1, 6))                   #Random szam generator
    print("dobások: ", end="")
    print(list_of_roll)

    for j in range(len(list_of_roll)):                                      #Attackerek és defenderek kiválasztása
        it += 1
        if inp_atk >= it:
            al.append(str(list_of_roll[j]))
        else:
            dl.append(str(list_of_roll[j]))

    for l in range(len(al)):                                                #Lista elemeinek string-be töltése
        atk += al[l] + "-"
    print("\n")

    for k in range(len(dl)):
        defe += dl[k] + "-"
    print("Dice:\n")
    print("   Attacker: " + atk[:-1])
    print("   Defender: " + defe[:-1] + "\n\n")
    if len(al) >= len(dl):                                                  #Harc loop hosszának eldöntése
        for_len = len(al)
    else:
        for_len = len(dl)

    for m in range(for_len):                                                #Elesett katonák számolása
        while len(dl) > it2 and len(al) > it2:
            if dl[it2] >= al[it2]:
                atk_lost += 1
            elif al[it2] > dl[it2]:
                def_lost += 1
            it2 += 1
    print("Outcome:\n")

    if 1 >= atk_lost:
        print("   Attacker: Lost " + str(atk_lost) + " unit")
    elif atk_lost > 1:
        print("   Attacker: Lost " + str(atk_lost) + " units")
    if 1 >= def_lost:
        print("   Defender: Lost " + str(def_lost) + " unit")
    elif def_lost > 1:
        print("   Defender: Lost " + str(def_lost) + " units")


risk()