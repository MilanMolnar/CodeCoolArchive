def my_function(a):
    b = a - 2
    return b


c = 3
if c > 2:
    d = my_function(5)
    print(d)

#1, Describe the scope of the variables a, b, c and d in this example:
    #Answer: Scope of "a" and "b" is the function(my_function) and the scope of "c" and "d" is global.

#2, What is the lifetime of these variables? When will they be created and destroyed?
    #Answer: Variable "a" and "b"'s lifetime is just as long as the function(my_function) evaluates.
            #"c" and "d" is accessable from the point they are defined with a value throughtout the rest of the program

#3, Can you guess what would happen if we were to assign c a value of 1 instead?
    #Answer: The if statement never evaluates to True and the function(my_function) is never called

#4, Why would this be a problem? Can you think of a way to avoid it?
    #Answer: First of all 1 is not greater than 2 so thats a problem, one way to work around this problem is to
            #lower the number we are comparing to or adding to the compared number(c) to be greater.