from reports import when_was_top_sold_fps, count_by_genre, count_games, decide, get_genres, get_latest, get_line_number_by_title, sort_abc

def input_tester(prompt):
    while True:
        try:
            x = int(input(prompt))
        except ValueError:
            print("Incorrect input! Please only use integers.")
            continue
        if isinstance(x, int):
            return x

# Export functions

def export_count_games():
    with open("export.txt", "w") as file_handler:
        file_handler.write("Total number of games in the file: " + str(count_games("game_stat.txt")) + ".\n\n")

def export_decide(prompt):
    with open("export.txt", "a") as file_handler:
        year = input_tester(prompt)
        if decide("game_stat.txt", year):
            file_handler.write("There is a game in the file published in " + str(year) + ".\n\n" )
        else:
            file_handler.write("There is no game in the file published in " + str(year) + ".\n\n")

def export_get_latest():
    with open("export.txt", "a") as file_handler:
        file_handler.write("The latest game relased in the file is: " + get_latest("game_stat.txt") + "\n\n")

def export_count_by_genre(prompt):
    with open("export.txt", "a") as file_handler:
        genre = input(prompt)
        file_handler.write("There is " + str(count_by_genre("game_stat.txt", genre)) + "games in the file under the " + str(genre) + " genre.\n\n")

def export_get_line_number_by_title(prompt):
    with open("export.txt", "a") as file_handler:
        title = input(prompt)
        file_handler.write(title.title() + " is found in line number " +  str(get_line_number_by_title("game_stat.txt", title)) + ".\n\n")

def export_sort_abc():
    with open("export.txt", "a") as file_handler:
        items = ""
        file_handler.write("The titles in this file in alphabetical order are as follows:\n")
        for item in range(len((sort_abc("game_stat.txt")))):
            items += '"' + (sort_abc("game_stat.txt"))[item] + '"' + ", "
            if item + 1 == len(sort_abc("game_stat.txt")):
                items = items[:-2]
                items += "."
        file_handler.write(items + "\n\n")

def export_get_genres():
    with open("export.txt", "a") as file_handler:
        genres = ""
        file_handler.write("All the genres in the file: ")
        for item in range(len((get_genres("game_stat.txt")))):
            genres += '"' + (get_genres("game_stat.txt"))[item] + '"' + ", "
            if item + 1 == len(get_genres("game_stat.txt")):
                genres = genres[:-2]
                genres += "."
        file_handler.write(genres)

def export_when_was_top_sold_fps():
    with open("export.txt", "a") as file_handler:
        file_handler.write("The top sold FPS was published in " + str(when_was_top_sold_fps("game_stat.txt")) + "." )

export_count_games()
export_decide("What year you want to test: ")
export_get_latest()
export_count_by_genre("What genre you want to test: ")
export_get_line_number_by_title("Which title you want to test: ")
export_sort_abc()
export_get_genres()
export_when_was_top_sold_fps()