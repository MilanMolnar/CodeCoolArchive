def IntTester(prompt):
    while True:
        try:
            x = int(input(prompt))
        except ValueError:
            print("Nem számot adtál meg!")
            continue
        if isinstance(x, int):
            return x


list_of_numbers = []

for i in range(0,8):
    if i == 0:
        prompt = "Adjon meg 8 számot: "
    else:
        prompt = "Adjon meg még " + str(8 - i) + " számot: "
    list_of_numbers.append(IntTester(prompt))
max = list_of_numbers[0]

for i in range(len(list_of_numbers)):
    for j in range(len(list_of_numbers)):
        if list_of_numbers[i] >= list_of_numbers[j]:
            if max < list_of_numbers[i]:
                max = list_of_numbers[i]

min = list_of_numbers[0]
for i in range(len(list_of_numbers)):
    for j in range(len(list_of_numbers)):
        if list_of_numbers[i] < list_of_numbers[j]:
            if min >= list_of_numbers[i]:
                min = list_of_numbers[i]

avg = 0
i = 0
while i < len(list_of_numbers):
   avg += list_of_numbers[i]
   i +=1

print("A megadott lista legnagyobb eleme: " + str(max))
print("A megadott lista legkisebb eleme: " + str(min))
print("A megadott lista átlaga: " + str(avg / len(list_of_numbers)))
