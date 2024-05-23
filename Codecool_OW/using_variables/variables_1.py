def apple_kilogra(priceprompt, kilogrammprompt):
    while True:
        try:
            price = int(input(priceprompt))
            volume = int(input(kilogrammprompt))
        except ValueError:
            print("Kerlek szamot adj meg")
            continue
        if isinstance(price, int) and isinstance(volume, int):
            break
    cost = int(price) * volume
    print(str(volume) + " kilogram alma " + str(cost) + " koronába kerül!")


apple_kilogra("Mennyibe kerül egy kg alma?: ", "Mennyi almát szeretnél venni?: ")
