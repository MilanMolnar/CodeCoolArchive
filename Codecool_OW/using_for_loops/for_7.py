def fibo():
    list_of_fibonacci = []
    n = 18
    it = 0
    for i in range(n):
        while it < 2:
            list_of_fibonacci.append(1)
            it += 1
            if it >= 2:
                break
        y = list_of_fibonacci[i] + list_of_fibonacci[i + 1]
        list_of_fibonacci.append(y)
    print(list_of_fibonacci)

fibo()