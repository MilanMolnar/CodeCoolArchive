list_of_numbers_1_to_99 = []
list_of_numbers_1_to_49 = []
for i in range(10):
    list_of_numbers_1_to_99.append(random.randint(1,99))

for i in range(10):
    guessing = int(input("Enter an integer from 1 to 99: "))
    while list_of_numbers_1_to_99[i] != guessing:
        if guessing < list_of_numbers_1_to_99[i]:
            print("Guess is low!")
            guessing = int(input("Enter an integer from 1 to 99: "))
        elif guessing > list_of_numbers_1_to_99[i]:
            print("Guess is high!")
            guessing = int(input("Enter an integer from 1 to 99: "))
        else:
            break
    print("You guessed it!")


for i in range(10):
    list_of_numbers_1_to_49.append(random.randint(1, 49))

for i in range(10):
    guess = int(input("Enter an integer from 1 to 49: "))
    while list_of_numbers_1_to_49[i] != guess:
        if guess < list_of_numbers_1_to_49[i]:
            print("Guess is low!")
            guess = int(input("Enter an integer from 1 to 49: "))
        elif guess > list_of_numbers_1_to_49[i]:
            print("Guess is high!")
            guess = int(input("Enter an integer from 1 to 49: "))
        else:
            break
    print("You guessed it!")
