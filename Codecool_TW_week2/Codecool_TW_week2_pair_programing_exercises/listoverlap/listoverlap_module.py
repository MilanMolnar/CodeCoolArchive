def listoverlap(a, b):
    c = []
    for i in b:
        for j in a:
            if i == j and i not in c:
                c.append(i)
    return c


def main():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    x = listoverlap(a,b)
    return x
#-----------------------------------------------------------------------------------------------------------------------
from random import randint

def listoverlap1(a, b):
    c = []
    for i in b:
        for j in a:
            if i == j and i not in c:
                c.append(i)
    return c


def main1():
    a = []
    b = []

    list_lenght_a=randint(5,20)
    list_lenght_b = randint(5, 20)

    for i in range(list_lenght_a):
        a.append(randint(1,100))

    for j in range(list_lenght_b):
        b.append(randint(1,100))

    print(a,b)
    x = listoverlap(a,b)
    return x

#-----------------------------------------------------------------------------------------------------------------------

def listoverlap2(a, b):
    return [list(filter(lambda x: x in a, sublist)) for sublist in b] #eltulajdonitott


def main2():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    x = listoverlap(a,b)
    return x

main2()

