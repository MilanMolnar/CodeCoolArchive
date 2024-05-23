import sys

if 2 > len(sys.argv):
    print('Nem adott meg fájlt!')
    exit()

filename = sys.argv[1]
csv_source = open(filename, "r")
csv = csv_source.readlines()

for word1 in csv:
    for word2 in csv:
        if sorted(word1) == sorted(word2) and word1 != word2:
            print(word1[:-1] + " " + word2[:-1] + "\n")