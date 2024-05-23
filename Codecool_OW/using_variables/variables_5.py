def korona_coin(fiveprompt, twoprompt, oneprompt):
    while True:
        try:
            five = int(input(fiveprompt))
            two = int(input(twoprompt))
            one = int(input(oneprompt))
        except ValueError:
            print("Kérem számot adjon meg!")
            continue
        if isinstance(five, int) and isinstance(two, int) and isinstance(one, int):
            break

    five_coins_value = five * 5
    two_coins_value = two * 2
    one_coins_value = one

    total = five_coins_value + two_coins_value + one_coins_value
    print("\nAz önnél lévő korona érmék összege: " + str(total))


korona_coin("Kérem adja meg mennyi 5 koronás érmével rendelkezik: ", "Kérem adja meg mennyi 2 koronás érmével rendelkezik: ", "Kérem adja meg mennyi 1 koronás érmével rendelkezik: ")