# Report functions

def get_most_played(file_name):                               #Part2/test1
    with open(file_name, "r") as file_handler:
        lines = file_handler.readlines()
        list_of_game_sold = []
        for line in lines:
            f_line = line.split('\t')
            list_of_game_sold.append(float(f_line[1]))
        max_sold = max(list_of_game_sold)
        for line in lines:
            f_line = line.split('\t')
            if float(f_line[1]) == float(max_sold):
                return (f_line[0])

def sum_sold(file_name):                                      #Part2/test2
    with open(file_name, "r") as file_handler:
        lines = file_handler.readlines()
        list_of_incomes = []
        for line in lines:
            f_line = line.split('\t')
            list_of_incomes.append(float(f_line[1]))
        return float(sum(list_of_incomes))

def get_selling_avg(file_name):                               #Part2/test3
    with open(file_name, "r") as file_handler:
        lines = file_handler.readlines()
        list_of_incomes = []
        for line in lines:
            f_line = line.split('\t')
            list_of_incomes.append(float(f_line[1]))
        return float(sum(list_of_incomes)) / len(list_of_incomes)

def count_longest_title(file_name):                           #Part2/test4
    with open(file_name, "r") as file_handler:
        lines = file_handler.readlines()
        list_of_title_lens = []
        for line in lines:
            f_line = line.split('\t')
            list_of_title_lens.append(len(f_line[0]))
        return max(list_of_title_lens)

def get_date_avg(file_name):                                  #Part2/test5
    with open(file_name, "r") as file_handler:
        lines = file_handler.readlines()
        list_of_reldate = []
        for line in lines:
            f_line = line.split('\t')
            list_of_reldate.append(float(f_line[2]))
        avg_reldate = float(sum(list_of_reldate)) / len(list_of_reldate)
        return round(avg_reldate)

def get_game(file_name, title):                               #Part2/test6
    if title:
        ret_list = []
        with open(file_name, "r") as file_handler:
            lines = file_handler.readlines()
            for line in lines:
                f_line = line.split('\t')
                if f_line[0] in title:
                    ret_list.append(f_line[0])
                    ret_list.append(float(f_line[1]))
                    ret_list.append(int(f_line[2]))
                    ret_list.append(f_line[3])
                    ret_list.append(f_line[4][:-1])
                    return ret_list
    return None


def count_grouped_by_genre(file_name):                       #Part2/bonus_test1
    with open(file_name, "r") as file_handler:
        lines = file_handler.readlines()
        list_of_genres = []
        for line in lines:
            f_line = line.split('\t')
            if f_line[3] not in list_of_genres:
                list_of_genres.append(f_line[3])
            else:
                continue
    with open(file_name, "r") as file_handler:
        dic_of_genres = {}
        lines = file_handler.readlines()
        for i in range(len(list_of_genres)):
            k=0
            for j in range(len(lines)):
                f_line = lines[j].split('\t')
                if f_line[3] == list_of_genres[i]:
                    k += 1
            dic_of_genres.update({list_of_genres[i]: k})
        return dic_of_genres

def get_date_ordered(file_name):
    title_year_dict = {}
    res_list = []
    with open(file_name, "r") as file_handler:
        lines = file_handler.readlines()
        for line in lines:
            f_line = line.split('\t')
            title_year_dict.update({f_line[0]:f_line[2]})
    sorted_dict = dict(sorted(title_year_dict.items(), key=lambda x: x[1], reverse=True))
    for key in sorted_dict:
        sorted_dict[key] = int(sorted_dict[key])
    list_of_tuples = [(key, value) for key, value in sorted_dict.items()]
    result_dict = dict(sorted(list_of_tuples, key=lambda tup: (-tup[1], tup[0])))
    for key in result_dict:
        res_list.append(key)
    return res_list
