mod_num = []
for i in range(1, 1000):
    if i % 9 == 0 or i % 7 == 0:
        mod_num.append(i)
mod_num.reverse()
for i in range(1,26):
    if 9 >= i:
        print(str(i) + ".  " + str(mod_num[i]))
    else:
        print(str(i) + ". " + str(mod_num[i]))
