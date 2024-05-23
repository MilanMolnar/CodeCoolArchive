import sys

def IntTester(prompt):
    while True:
        try:
            x = int(input(prompt))
        except ValueError:
            print("Nem számot adtál meg!")
            continue
        if isinstance(x, int):
            return x


main_question = input("Add meg pontosan mit szeretnél csinálni [lista], [megjelol], [hozzaad], [archival]: ")
file = open("ideas.txt", "a")
num = 1
marked_lines = []
index_list = []

with open("archive_index.txt") as indexlol:
    indexlines = indexlol.readlines()
    for z in range(len(indexlines)):
        index_list.append(int(indexlines[z]))
if main_question == "hozzaad":
    while True:
        x = input("Jegyezd fel a feladatod: ")
        for line in open("ideas.txt").readlines(): num += 1
        file.write(x + "\n")
        break
    file = open('ideas.txt', 'r')
    for i, line in enumerate(file, start=1):
        if int(i) in index_list:
            print('{}.[x] {}'.format(i, line.strip()))
        elif int(i) not in index_list:
            print('{}.[ ] {}'.format(i, line.strip()))
else:
    if main_question in "lista":
        file = open("ideas.txt", "r")
        print("A feladataid, kilistázva: ")
        for i, line in enumerate(file, start=1):
            if int(i) in index_list:
                print('{}.[x] {}'.format(i, line.strip()))
            elif int(i) not in index_list:
                print('{}.[ ] {}'.format(i, line.strip()))
    elif main_question in "megjelol":
        file = open("ideas.txt", "r")
        print("feladataid kilistázava: ")
        for i, line in enumerate(file, start=1):
            if int(i) in index_list:
                print('{}.[x] {}'.format(i, line.strip()))
            elif int(i) not in index_list:
                print('{}.[ ] {}'.format(i, line.strip()))
        mark_num = IntTester("Add meg számmal, hogy melyik elemet szeretnéd megjelölni: ")
        with open("archive_index.txt", "a") as archive_indes_num:
            archive_indes_num.write(str(mark_num) + "\n")
        file = open("ideas.txt", "r")
        print("A megjelölt feladataid:")
        for i, line in enumerate(file, start=1):
            if i == mark_num or int(i) in index_list:
                print('{}.[x] {}'.format(i, line.strip()))
            elif i != mark_num or int(i) not in index_list:
                print('{}.[ ] {}'.format(i, line.strip()))
    elif main_question in "archival":
        with open("ideas.txt", "r") as ideas_archive:
            with open("archive_index.txt", "r") as index_read:
                for i, line in enumerate(ideas_archive, start = 1):
                    if i == index_read.readline():
                        with open("Archive_ideas.txt", "a") as archive:
                            lines = file.readlines()
                            archive.write(lines)
                        with open("ideas.txt", "r+") as file:
                            lines = file.readlines()
                            del lines
                            file.seek(0)
                            file.truncate()
                            file.writelines(lines)
        file = open('ideas.txt', 'r+')
        index_read = open("archive_index.txt", "r+")
        lines_i = index_read.readlines()
        ideas = open("ideas.txt", "r")
        lines = ideas.readlines()
        k = 0
        list_index = []
        print("Archivált feladatok:")
        for i in range(len(lines)):
            k += 1
            for j in lines_i:
                if str(k) == str(j[:-1]):
                    list_index.append(int(j[:-1]))
        list_index.sort()
        list_index.reverse()
        for z in range(len(list_index)):
            with open("ideas.txt", "r+") as file:
                lines = file.readlines()
                print(lines[list_index[z] - 1])
                with open("todo_done.txt", "a") as todo_done:
                    todo_done.writelines(str(lines[list_index[z]-1]) + "\n")
                del lines[list_index[z]-1]
                file.seek(0)
                file.truncate()
                file.writelines(lines)
        with open("archive_index.txt", "w") as delete_index:
            delete_index.seek(0)
            delete_index.truncate()



