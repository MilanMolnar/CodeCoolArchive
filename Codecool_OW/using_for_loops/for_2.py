def factorial():
    x = 1
    for i in range(7):
        x += x * i
    return x


y = factorial()
print(y)