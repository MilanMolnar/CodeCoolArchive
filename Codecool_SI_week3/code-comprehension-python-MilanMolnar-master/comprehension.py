#Guessing game with the guess being between 1-20 and the possible number of guesses being 6.

import random #Importing module(random)

guesses_taken = 0 #Assigning value to guesses_taken

print('Hello! What is your name?') #Printing to console
myName = input() #Assinging userinput to variable(myName)

number = random.randint(1, 20) #Assigning 1-20 random int to variable(number)
print('Well, ' + myName + ', I am thinking of a number between 1 and 20.') #Printing the string with a variable

while guesses_taken < 6: #Starting a loop as long as the variable(guesses_taken) is less then 6
    print('Take a guess.') #Pringing a string
    guess = input() #Assigning the input value to variable(guess)
    guess = int(guess) #Converting input to integer

    guesses_taken += 1 #Incrementing variable(guesses_taken) by 1

    if guess < number: #Condition guess less than number
        print('Your guess is too low.') #Printing a string if above condition is met.

    if guess > number: #Condition number less than guess
        print('Your guess is too high.') #Printing a string if above condition is met.

    if guess == number: #Condition number equals to guess
        break #Breaks the cycle if above condition is met

if guess == number: #Condition number equals to guess
    guesses_taken = str(guesses_taken) #Converting variable(guesses_taken) to string
    print('Good job, ' + myName + '! You guessed my number in ' + guesses_taken + ' guesses!') #Printing winning state

if guess != number: #Condition number equals to guess
    number = str(number) #Converting variable(number) to string
    print('Nope. The number I was thinking of was ' + number) #Printing losing state
