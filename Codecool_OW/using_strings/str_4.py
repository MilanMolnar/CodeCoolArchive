def chara(widthprompt, charprompt):
    while True:
        try:
            width = int(input(widthprompt))
        except ValueError:
            print("Kérlek szlmot adj meg!")
            continue
        if isinstance(width, int):
            break
    char = input(charprompt)

    for i in range(width):
        print(width * char)

chara("Irj be egy szamot: ","irj be egy karaktert: ")