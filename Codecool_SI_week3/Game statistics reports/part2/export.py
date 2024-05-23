from reports2 import get_most_played, sum_sold, get_selling_avg, count_longest_title, get_date_avg, get_game, \
    count_grouped_by_genre, get_date_ordered
# Export functions

def export_get_most_played():
    with open("export.txt", "w") as file_handler:
        file_handler.write("The title of the most played game in the file is: " + get_most_played("game_stat.txt") + ".\n")

def export_sum_sold():
    with open("export.txt", "a") as file_handler:
        file_handler.write(str(sum_sold("game_stat.txt"))+ " million copies have been sold total according to the file.\n")

def export_get_selling_avg():
    avg_float = get_selling_avg("game_stat.txt")
    with open("export.txt", "a") as file_handler:
        file_handler.write(str(avg_float) + "is the average selling according to the file.\n")

def export_count_longest_title():
    with open("export.txt", "a") as file_handler:
        file_handler.write(str(count_longest_title("game_stat.txt")) + " characters long is the longest title in the file.\n")

def export_get_date_avg():
    with open("export.txt", "a") as file_handler:
        file_handler.write(str(get_date_avg("game_stat.txt")) + " is the average of the release dates in the file\n")

def export_get_game(prompt):
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
    with open("export.txt", "a") as file_handler:
        file_handler.write(title + "'s genre is '"+ print_list[3]+ "' was relased in " + print_list[2] + " sold over "+ print_list[1] +
              " million copies and currently owned by: " + print_list[4] + ".\n")

def export_count_grouped_by_genre():
    print_dic = count_grouped_by_genre("game_stat.txt")
    for key in print_dic:
        with open("export.txt", "a") as file_handler:
            file_handler.write(str(key) + " genre has " + str(print_dic[key]) + " games in the file.\n")

def export_get_date_ordered():
    items = ""
    print_list = []
    for i in range(len(get_date_ordered("game_stat.txt"))):
        print_list.append(str(get_date_ordered("game_stat.txt")[i]))
    for item in range(len(print_list)):
        items += '"' + print_list[item] + '"' + ", "
        if item + 1 == len(print_list):
            items = items[:-2]
            items += "."
    with open("export.txt", "a") as file_handler:
        file_handler.write("The date in which the games were ordered in the file are as follows " + items)


export_get_most_played()

export_sum_sold()

export_get_selling_avg()

export_count_longest_title()

export_get_date_avg()

export_get_game("Input the title of the game: ")

export_count_grouped_by_genre()

export_get_date_ordered()