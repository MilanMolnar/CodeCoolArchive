from reports2 import get_most_played, sum_sold, get_selling_avg, count_longest_title, get_date_avg, get_game, \
    count_grouped_by_genre, get_date_ordered
# Printing functions

def print_get_most_played():
    print("The title of the most played game in the file is:", get_most_played("game_stat.txt") + ".")

def print_sum_sold():
    print(str(sum_sold("game_stat.txt")), "million copies have been sold total according to the file.")

def print_get_selling_avg():
    avg_float = get_selling_avg("game_stat.txt")
    print(str(avg_float) + "is the average selling according to the file.")

def print_count_longest_title():
    print(count_longest_title("game_stat.txt"), "characters long is the longest title in the file.")

def print_get_date_avg():
    print(get_date_avg("game_stat.txt"),"is the average of the release dates in the file")

def print_get_game(prompt):
    items = ""
    title = input(prompt)
    print_list = []
    for i in range(len(get_game("game_stat.txt", title))):
        print_list.append(str(get_game("game_stat.txt", title)[i]))
    for item in range(len(print_list)):
        items += '"' + print_list[item] + '"' + ", "
        if item + 1 == len(print_list):
            items = items[:-2]
            items += "."
    print(title + "'s data in the file are the following:", items)
    question = input("Do you want a detailed verison[y/n]")
    if question in ["y","Y"]:
        print(title + "'s genre is '"+ print_list[3]+ "' was relased in", print_list[2], "sold over",print_list[1],
              "million copies and currently owned by:", print_list[4] + ".")
    else:
        print("Have a nice day!")

def print_count_grouped_by_genre():
    print_dic = count_grouped_by_genre("game_stat.txt")
    for key in print_dic:
        print(key, "genre has", print_dic[key], "games in the file.")

def print_get_date_ordered():
    items = ""
    print_list = []
    for i in range(len(get_date_ordered("game_stat.txt"))):
        print_list.append(str(get_date_ordered("game_stat.txt")[i]))
    for item in range(len(print_list)):
        items += '"' + print_list[item] + '"' + ", "
        if item + 1 == len(print_list):
            items = items[:-2]
            items += "."
    print("The date in which the games were ordered in the file are as follows " + items)

print("\n\nWhat is the title of the most played game (i.e. sold the most copies)?")
print_get_most_played()
print("\n\nHow many copies have been sold total?")
print_sum_sold()
print("\n\nWhat is the average selling?")
print_get_selling_avg()
print("\n\nHow many characters long is the longest title?")
print_count_longest_title()
print("\n\nWhat is the average of the release dates?")
print_get_date_avg()
print("\n\nWhat properties has a game?")
print_get_game("Input the title of the game: ")
print("\n\nHow many games are there grouped by genre?")
print_count_grouped_by_genre()
print("\n\nWhat is the date ordered list of the games?")
print_get_date_ordered()