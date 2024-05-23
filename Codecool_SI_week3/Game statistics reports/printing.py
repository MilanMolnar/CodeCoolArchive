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

# Printing functions

def print_count_games():
    print("Total number of games in the file: " + str(count_games("game_stat.txt")) + ".")

def print_decide(prompt):
    year = input_tester(prompt)
    if decide("game_stat.txt", year):
        print("There is a game in the file published in", str(year) + "." )
    else:
        print("There is no game in the file published in", str(year) + ".")

def print_get_latest():
    print("The latest game relased in the file is:",get_latest("game_stat.txt"))

def print_count_by_genre(prompt):
    genre = input(prompt)
    print("There is", count_by_genre("game_stat.txt", genre), "games in the file under the", genre, "genre.")

def print_get_line_number_by_title(prompt):
    title = input(prompt)
    print(title.title(),"is found in line number", str(get_line_number_by_title("game_stat.txt", title)) + ".")

def print_sort_abc():
    items = ""
    print("The titles in this file in alphabetical order are as follows:\n", end="")
    for item in range(len((sort_abc("game_stat.txt")))):
        items += '"' + (sort_abc("game_stat.txt"))[item] +  '"'+ ", "
        if item + 1 == len(sort_abc("game_stat.txt")):
            items = items[:-2]
            items += "."
    print(items)

def print_get_genres():
    genres = ""
    print("All the genres in the file: ", end="")
    for item in range(len((get_genres("game_stat.txt")))):
        genres += '"' + (get_genres("game_stat.txt"))[item] +  '"'+ ", "
        if item + 1 == len(get_genres("game_stat.txt")):
            genres = genres[:-2]
            genres += "."
    print(genres)

def print_when_was_top_sold_fps():
    print("The top sold FPS was published in", str(when_was_top_sold_fps("game_stat.txt")) + "." )

print("How many games are in the file?")
print_count_games()
print("\n\nIs there a game from a given year?")
print_decide("What year you want to test: ")
print("\n\nWhich was the latest game?")
print_get_latest()
print("\n\nHow many games do we have by genre?")
print_count_by_genre("What genre you want to test: ")
print("\n\nWhat is the line number of the given game (by title)?")
print_get_line_number_by_title("Which title you want to test: ")
print("\n\nWhat is the alphabetical ordered list of the titles?")
print_sort_abc()
print("\n\nWhat are the genres?")
print_get_genres()
print('\n\nWhat is the release date of the top sold "First-person shooter" game?')
print_when_was_top_sold_fps()
