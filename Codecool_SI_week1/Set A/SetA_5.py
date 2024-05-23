import sys


file = open("ideas.txt", "a")
num = 1
try:
    if len(sys.argv) == 1:
        while True:
            x = input("What is your new idea: ")
            for line in open("ideas.txt").readlines(): num += 1
            file.write(x + "\n")
            break
        file = open('ideas.txt', 'r')
        for i, line in enumerate(file, start=1):
            print('{}. {}'.format(i, line.strip()))
    else:
        if sys.argv[1] == "--list":
            file = open("ideas.txt", "r")
            print("Your ideabank:")
            for i, line in enumerate(file, start=1):
                print('{}. {}'.format(i, line.strip()))
        elif sys.argv[1] in "--delete":
            arg_num = int(sys.argv[2]) - 1
            with open("ideas.txt", "r+") as file:
                lines = file.readlines()
                del lines[arg_num]
                file.seek(0)
                file.truncate()
                file.writelines(lines)
            file = open('ideas.txt', 'r')
            for i, line in enumerate(file, start=1):
                print('{}. {}'.format(i, line.strip()))
except:
    print("Upsz, valamit elirtál!")


