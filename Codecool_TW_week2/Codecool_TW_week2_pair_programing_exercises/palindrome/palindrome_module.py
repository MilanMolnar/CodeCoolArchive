def palindrome(str):
    list_str = []
    for letter in str:
        if letter != " ":
            list_str.append(letter.lower())
    rev_list_str = list_str[::-1]
    if list_str == rev_list_str:
        return True
    else:
        return False


def main():
    str = input("Írj be egy stringet: ")
    palindrome(str)
    return

main()


