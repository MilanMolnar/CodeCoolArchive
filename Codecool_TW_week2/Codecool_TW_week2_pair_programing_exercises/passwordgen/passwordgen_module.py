from random import randint
def passwordgen():
    while True:
        y = input("Milyen erős jelszót szeretnél[Strong/Medium/Weak/Test]: ")
        if y == "Strong":
            password=[]
            leng=randint(8,20)

            for i in range(leng):
                randomchar=chr(randint(33,126))            #33-126
                password.append(randomchar)
            password_str = ""
            for i in range(len(password)):
                password_str += password[i]
            return password_str
        elif y == "Weak":
            w_pw = ["dog", "1234", "qwertz", "jelszo", "gyengejelszoxd"]
            password = w_pw[randint(0,4)]
            return password
        elif y == "Medium":
            password = ""
            m_pw = [chr(randint(48, 57)), chr(randint(65, 90)), chr(randint(97, 122))]
            password += m_pw[randint(0)]
            for i in range(randint(8,12)):
                m_pw = [chr(randint(48, 57)), chr(randint(65, 90)), chr(randint(97, 122))]
                password += m_pw[randint(0, 2)]
            return password
        elif y == "Test":
            password = ""
            m_pw = [chr(randint(0, 9)), chr(randint(65, 90)), chr(randint(97, 122)),chr(94)]
            password += m_pw[0]
            password += m_pw[1]
            password += m_pw[2]
            password += m_pw[3]
            for i in range(randint(4,8)):
                m_pw = [chr(randint(48, 57)), chr(randint(65, 90)), chr(randint(97, 122))]
                password += m_pw[randint(0, 2)]
            return password
        else:
            print("Válasszon az felsorolt opciókból [Weak/Meadium/Strong/Test]")
            continue


def main():
    x=input("Szeretnél új jelszót [y/n]: ")
    if x in ["y", "Y"]:
        x = passwordgen()
    else:
        print("Viszlát!")
        exit()
    return x

x=main()
print(x)


