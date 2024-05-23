def list_input(lp, np):
    l = int(input(lp))
    numbers = []
    for i in range(l):
        numbers.append(int(input()))
    return numbers

def core(j):
    temp = numbers[j + 1]
    numbers[j + 1] = numbers[j]
    numbers[j] = temp
    j += 1
    return temp

def body(iterations):
    N = len(numbers)
    print(numbers)
    while N > iterations:
        j = 0
        while N - 2 >= j:
            if numbers[j] > numbers[j + 1]:
                core(j)
            else:
                j += 1
        else:
            iterations += 1
    else:
        print(numbers)

numbers = list_input("Mennyi számot szeretnél megadni: ", "Irj be számokat: " )
body(1)