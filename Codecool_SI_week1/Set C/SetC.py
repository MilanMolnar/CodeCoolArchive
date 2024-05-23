
l = int(input("Mennyi számot szeretnél megadni: "))
numbers = []
for i in range(l):
    numbers.append(int(input("Irj be számokat: ")))

N = len(numbers)
print(numbers)
iterations = 1
while N > iterations:
    j = 0
    while N - 2 >= j:
        if numbers[j] > numbers[j + 1]:
            temp = numbers[j + 1]
            numbers[j + 1] = numbers[j]
            numbers[j] = temp
            j += 1
        else:
            j += 1
    else:
        iterations += 1
else:
    print(numbers)


