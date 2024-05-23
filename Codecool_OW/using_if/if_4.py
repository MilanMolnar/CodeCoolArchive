def easter():
    while True:
        try:
            T = int(input("Irjon be egy évet: "))
        except ValueError:
            print("Szamokkal adja meg az évet")
        if T > 2099 and 1800 < T:
            print("Kérem évszámot adjon meg 1800 ls 2099 között")
        else:
            break

    A = T % 19
    B = T % 4
    C = T % 7
    D = (19 * A + 24) % 30
    E = (2 * B + 4 * C + 6 * D + 5) % 7
    H = 22 + D + E
    if H <= 31:
        print(str(T) + ". évben " + "Március " + str(H) + "-ra esik húsvét első vasárnapja.")
    else:
        H = H - 31
        print(str(T) + ". évben " + "Április " + str(H) + "-ra esik húsvét első vasárnapja.")
    if E == 6 and D == 29:
        H = 50
    elif E == 6 and D == 28:
        H = 49

easter()



