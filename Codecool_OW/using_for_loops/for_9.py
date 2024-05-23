def factorial_calculator(fprompt):
    while True:
        try:
            f = int(input(fprompt))
        except ValueError:
            print("Kérlek számot adj meg!")
            continue
        if isinstance(f, int):
            break
    factorial = 1
    for x in range(1, f+1):
        factorial = factorial * x
    return factorial


factorial_value = factorial_calculator("Irj be egy szamot: ")
print(factorial_value)