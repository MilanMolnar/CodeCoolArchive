import sys

if 2 > len(sys.argv):
    print('Nem adott meg igét')
    exit()

vowels = ["a", "e", "i", "o", "u"]
constants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "x", "z", "w", "y"]
exceptions = ["be", "see", "flee", "knee"]
for i in range(len(sys.argv)):
    if i >= 1:
        if sys.argv[i][-1] in constants and sys.argv[i][-2] in vowels and sys.argv[i][-3] in constants:
            print(sys.argv[i] + sys.argv[i][-1] + "ing")
        elif sys.argv[i][-1] == "e" and sys.argv[i] in exceptions:
            print(sys.argv[i] + "ing")
        elif sys.argv[i][-1] == "e" and sys.argv[i][-2] == "i":
            orig = sys.argv[i]
            convert_orig = orig[:-2]
            print(convert_orig + "ying")
        elif sys.argv[i][-1] == "e":
            orig = sys.argv[i]
            convert_orig = orig[:-1]
            print(convert_orig + "ing")
        else:
            print(sys.argv[i] + "ing")
