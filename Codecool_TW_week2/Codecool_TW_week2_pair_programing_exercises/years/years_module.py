import datetime


def years(age):
    age_t_100=2019+(100-age)
    return age_t_100


def main():
    input("type your name:")
    age=int(input("type your age:"))
    how_many=int(input("how many times?"))
    x = years(age)
    for i in range(1,how_many):
        print(x)
    print(x)
    return x

main()