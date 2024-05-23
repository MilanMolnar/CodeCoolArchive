def float_input(prompt):
    while True:
        try:
            x = float(input(prompt))
        except ValueError:
            print("Kérem adjon meg számot!")
            continue
        else:
            return x

def celsius_calc():
    T_f = float_input("Add meg a hőmérsékletet fahrentheitben: ")
    T_c = (T_f - 32) / 1.8   #(T(°F) - 32) / 1.8
    print(T_c)
    return T_c

celsius_calc()