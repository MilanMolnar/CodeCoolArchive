def odd():
    x = 0
    for i in range(101):
        x += (i*2) - 1
    return x


x = odd()
print(x)