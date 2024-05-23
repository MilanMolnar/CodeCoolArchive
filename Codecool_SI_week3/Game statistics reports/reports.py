def sorting(list):                                      #Buble sorting algorithm
    sorted = False
    while sorted == False:
        sorted = True
        for obj in range(len(list) - 1):
            if list[obj] > list[obj + 1]:
                temp = list[obj]
                list[obj] = list[obj + 1]
                list[obj + 1] = temp
                sorted = False
    return list

# Report functions

def count_games(file_name):                                 #Test1
    with open(file_name, "r") as file_handler:
        number_of_games = 0
        for lines in file_handler:
            number_of_games += 1
    return number_of_games

def decide(file_name, year):                                #Test2
    with open(file_name, "r") as file_handler:
        lines = file_handler.read()
        if str(year) in lines:
            return True
        else:
            return False

def get_latest(file_name):                                  #Test3
    with open(file_name, "r") as file_handler:
        lines = file_handler.readlines()
        list_of_game_year = []
        for line in lines:
            f_line = line.split('\t')
            list_of_game_year.append(f_line[2])
        latest_year = max(list_of_game_year)
        for line in lines:
            f_line = line.split('\t')
            if f_line[2] == latest_year:
                return f_line[0]

def count_by_genre(file_name, genre):                       #Test4
    with open(file_name, "r") as file_handler:
        lines = file_handler.readlines()
        num_of_games_by_genre = 0
        for line in lines:
            f_line = line.split('\t')
            if f_line[3].lower() == genre.lower():
                num_of_games_by_genre += 1
    return num_of_games_by_genre

def get_line_number_by_title(file_name, title):             #Test5
    with open(file_name, "r") as file_handler:
        num_of_line = 0
        lines = file_handler.readlines()
        for line in lines:
            f_line = line.split('\t')
            num_of_line += 1
            if f_line[0].lower() == title.lower():
                return num_of_line
        raise ValueError

def sort_abc(file_name):                                    #Bonus Test1
    list_of_titles = []
    with open(file_name, "r") as file_handler:
        lines = file_handler.readlines()
        for line in lines:
            f_line = line.split('\t')
            list_of_titles.append(f_line[0])
        return sorting(list_of_titles)

def get_genres(file_name):                                  #Bonus Test2
    list_of_genres = []
    list_of_genres_cutted = []
    with open(file_name, "r") as file_handler:
        lines = file_handler.readlines()
        for line in lines:
            f_line = line.split('\t')
            list_of_genres.append(f_line[3])
    for genre in list_of_genres:
        if genre not in list_of_genres_cutted:
            list_of_genres_cutted.append(genre)
    return sorting(list_of_genres_cutted)

def when_was_top_sold_fps(file_name):                       #Bonus Test3
    with open(file_name, "r") as file_handler:
        lines = file_handler.readlines()
        list_of_game_sold = []
        for line in lines:
            f_line = line.split('\t')
            if f_line[3] == "First-person shooter":
                list_of_game_sold.append(float(f_line[1]))
        max_sold = max(list_of_game_sold)
        for line in lines:
            f_line = line.split('\t')
            if float(f_line[1]) == float(max_sold):
                return int(f_line[2])


