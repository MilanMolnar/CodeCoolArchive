import time
import sys


def sprint(str):
    for c in str + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.8 / 1)

def exitu(exit_parameter):
    while True:
        e = input(exit_parameter)
        if e == "exit":
            exit()
        elif e == "start":
            break

def get_number_from_console(parameter):
    value = None
    while True:
        try:
            value = float(input(parameter))
        except ValueError:
            print("Kerkek szamot adj meg!")
            continue

        if isinstance(value, float):
            break
    return value


def operation_read(operation_sign):
    while True:
        value_operator = input(operation_sign)
        if value_operator in ("+", "-", "*", "/"):
            break
        else:
            print("Nem megfelelő operátor!")
            continue
    return value_operator


def calculator(operator, number_one, number_two):
    try:
        if operator == "+":
            print("A szamolas eltarthat pár masodpercig", end="")
            sprint("...")
            print("Eredmeny = ", number_one + number_two)

        elif operator == "-":
            print("A szamolas eltarthat pár masodpercig", end="")
            sprint("...")
            print("Eredmeny = ", number_one - number_two)

        elif operator == "*":
            print("A szamolas eltarthat pár masodpercig", end="")
            sprint("...")
            print("Eredmeny = ", number_one * number_two)

        elif operator == "/":
            print("A szamolas eltarthat pár masodpercig", end="")
            sprint("...")
            print("Eredmeny = ", number_one / number_two)
    except:
        print("Nullával nem lehet osztani!")
    while True:
        repeat = input("Szeretnéd még használni a számológépet? [y/n]\n:")
        if repeat in ["y","Y"]:
            print("\"Y\"-t nyomtál")
            x = get_number_from_console("Adj meg egy szamot: ")
            z = operation_read("Ird be az operátort: ")
            y = get_number_from_console("Adj meg egy másik szamot: ")
            calculator(z, x, y)
            break
        elif repeat in ["n", "N"]:
            print("\"N\"-t nyomtál\n")
            sprint("kilépés")
            exit()

exitu("Kezdéshez írja be, hogy \"start\", kilépéshez írd be, hogy \"exit\".\n:")
x = get_number_from_console("Adj meg egy szamot: ")
z = operation_read("Ird be az operátort: ")
y = get_number_from_console("Adj meg egy másik szamot: ")
calculator(z, x, y)


