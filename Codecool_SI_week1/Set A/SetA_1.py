import sys

def hello_user():
    if len(sys.argv) == 1:
        print("Hello World!")
    else:
        print("Hello " + str(sys.argv[1]))

def exit_message():
    print("A Flowchart itt érhető el: https://drive.google.com/open?id=12lr6ImVL6shpumYqFN2fRWBgdKQNGMih")
    input("Kilépéshez nyomj egy \"Enter\"-t")

hello_user()
exit_message()

