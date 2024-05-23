import time
import sys
import random
from msvcrt import getch
import os
import colorama
from math import inf as infinity
from random import choice
import platform
import time
from os import system
from screens import O_win, X_win, Draw_win, Human_win, AI_win, Title_screen



print("\n"* 8)
print(Title_screen)

def replaySingle():
    while True:
        restart = input("Do you want to play again? [Y/N]: ")

        if restart in ["y", "Y"]:
            print("New game!\n\n\n")
            single_player()
        elif restart is "N" or restart is "n":
            print("Have a nice day!")
            exit()
        else:
            print("Please input a correct answer!")
            continue


def replayMulti():
    while True:
        restart = input("Do you want to play again? [Y/N]: ")

        if restart in ["y", "Y"]:
            print("New game!\n\n\n")
            multi_player()
        elif restart is "N" or restart is "n":
            print("Have a nice day!")
            exit()
        else:
            print("Please input a correct answer!")
            continue


def replaySpec():
    while True:
        restart = input("Do you want to watch them again? [Y/N]: ")

        if restart in ["y", "Y"]:
            print("New game!\n\n\n")
            spectator_player()
        elif restart is "N" or restart is "n":
            print("Have a nice day!")
            exit()
        else:
            print("Please input a correct answer!")
            continue


def AILoad():
    for i in range(1, 5):
        sys.stdout.write('\rAI is choosing |')
        time.sleep(0.1)
        sys.stdout.write('\rAI is choosing   /')
        time.sleep(0.1)
        sys.stdout.write('\rAI is choosing   -')
        time.sleep(0.1)
        sys.stdout.write('\rAI is choosing   \\')
        time.sleep(0.1)
    sys.stdout.write('\rAI is choosing         ')
    print("\n")


def Ai_experimental():
    HUMAN = -1
    COMP = +1

    board = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
    ]
    changed_map = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
    ]

    def evaluate(state):

        if wins(state, COMP):
            score = +1
        elif wins(state, HUMAN):
            score = -1
        else:
            score = 0

        return score


    def wins(state, player):

        win_state = [
            [state[0][0], state[0][1], state[0][2]],
            [state[1][0], state[1][1], state[1][2]],
            [state[2][0], state[2][1], state[2][2]],
            [state[0][0], state[1][0], state[2][0]],
            [state[0][1], state[1][1], state[2][1]],
            [state[0][2], state[1][2], state[2][2]],
            [state[0][0], state[1][1], state[2][2]],
            [state[2][0], state[1][1], state[0][2]],
        ]
        if [player, player, player] in win_state:
            return True
        else:
            return False


    def game_over(state):

        return wins(state, HUMAN) or wins(state, COMP)


    def empty_cells(state):

        cells = []

        for x, row in enumerate(state):
            for y, cell in enumerate(row):
                if cell == 0:
                    cells.append([x, y])

        return cells


    def valid_move(x, y):

        if [x, y] in empty_cells(board):
            return True
        else:
            return False


    def set_move(x, y, player):

        if valid_move(x, y):
            board[x][y] = player
            return True
        else:
            return False


    def minimax(state, depth, player):
        if player == COMP:
            best = [-1, -1, -infinity]
        else:
            best = [-1, -1, +infinity]

        if depth == 0 or game_over(state):
            score = evaluate(state)
            return [-1, -1, score]

        for cell in empty_cells(state):
            x, y = cell[0], cell[1]
            state[x][y] = player
            score = minimax(state, depth - 1, -player)
            state[x][y] = 0
            score[0], score[1] = x, y

            if player == COMP:
                if score[2] > best[2]:
                    best = score  # max value
            else:
                if score[2] < best[2]:
                    best = score  # min value

        return best


    def clean():
        os_name = platform.system().lower()
        if 'windows' in os_name:
            system('cls')
        else:
            system('clear')


    def render(state, c_choice, h_choice):
        print(c_choice + h_choice)
        chars = {
            'X',
            'O',
            ' '
        }
        str_line = '---------------'
        print('\n' + str_line)
        x_c = -1
        y_c = -1
        changed_map = [
               [" ", " ", " "],
               [" ", " ", " "],
               [" ", " ", " "]
               ]
        for i in range(len(state)):
            for j in range(len(state[i])):
                if state[i][j] == -1:
                    changed_map[i][j] = "X"
                elif state[i][j] == 1:
                    changed_map[i][j] = 'O'
                else:
                    changed_map[i][j] = " "
        print(state)
        print(map)
        top = '''╔═══╦═══╦═══╗'''
        mid1 = '''║ ''' + changed_map[0][0] + ''' ║ ''' + changed_map[0][1] + ''' ║ ''' + changed_map[0][2] + ''' ║'''
        mids = '''╠═══╬═══╬═══╣'''
        mid2 = '''║ ''' + changed_map[1][0] + ''' ║ ''' + changed_map[1][1] + ''' ║ ''' + changed_map[1][2] + ''' ║'''
        mid3 = '''║ ''' + changed_map[2][0] + ''' ║ ''' + changed_map[2][1] + ''' ║ ''' + changed_map[2][2] + ''' ║'''
        bot = '''╚═══╩═══╩═══╝'''
        print("\n" * 30)
        print(73 * " " + (top))
        print(73 * " " + (mid1))
        print(73 * " " + (mids))
        print(73 * " " + (mid2))
        print(73 * " " + (mids))
        print(73 * " " + (mid3))
        print(73 * " " + (bot))
        print("\n" * 15)


    def ai_turn(c_choice, h_choice):

        depth = len(empty_cells(board))
        if depth == 0 or game_over(board):
            return

        clean()
        print(f'Computer turn [{c_choice}]')
        render(board, c_choice, h_choice)

        if depth == 9:
            x = choice([0, 1, 2])
            y = choice([0, 1, 2])
        else:
            move = minimax(board, depth, COMP)
            x, y = move[0], move[1]

        set_move(x, y, COMP)
        time.sleep(1)


    def human_turn(c_choice, h_choice):

        depth = len(empty_cells(board))
        if depth == 0 or game_over(board):
            return

        # Dictionary of valid moves
        move = -1
        moves = {
            1: [0, 0], 2: [0, 1], 3: [0, 2],
            4: [1, 0], 5: [1, 1], 6: [1, 2],
            7: [2, 0], 8: [2, 1], 9: [2, 2],
        }

        clean()
        print(f'Human turn [{h_choice}]')
        render(board, c_choice, h_choice)

        while move < 1 or move > 9:
            try:
                move = int(input('Use numpad (1..9): '))
                coord = moves[move]
                can_move = set_move(coord[0], coord[1], HUMAN)

                if not can_move:
                    print('Bad move')
                    move = -1
            except (EOFError, KeyboardInterrupt):
                print('Bye')
                exit()
            except (KeyError, ValueError):
                print('Bad choice')


    def main():

        clean()
        h_choice = ''  # X or O
        c_choice = ''  # X or O
        first = ''  # if human is the first
        c_choice = 'X'
        h_choice = 'O'

        # Human may starts first
        clean()
        while first != 'Y' and first != 'N':
            try:
                first = input('First to start?[y/n]: ').upper()
            except (EOFError, KeyboardInterrupt):
                print('Bye')
                exit()
            except (KeyError, ValueError):
                print('Bad choice')

        # Main loop of this game
        while len(empty_cells(board)) > 0 and not game_over(board):
            if first == 'N':
                ai_turn(c_choice, h_choice)
                first = ''

            human_turn(c_choice, h_choice)
            ai_turn(c_choice, h_choice)

        # Game over message
        if wins(board, HUMAN):
            clean()
            print(f'Human turn [{h_choice}]')
            render(board, c_choice, h_choice)
            print(Human_win)
        elif wins(board, COMP):
            clean()
            print(f'Computer turn [{c_choice}]')
            render(board, c_choice, h_choice)
            print(AI_win)
        else:
            clean()
            render(board, c_choice, h_choice)
            print(Draw_win)

        exit()
    main()


def multi_player():
    def x_win(map):
        if map[0][0] == "X" and map[0][1] == "X" and map[0][2] == "X":
            return True
        elif map[1][0] == "X" and map[1][1] == "X" and map[1][2] == "X":
            return True
        elif map[2][0] == "X" and map[2][1] == "X" and map[2][2] == "X":
            return True
        elif map[0][0] == "X" and map[1][0] == "X" and map[2][0] == "X":
            return True
        elif map[0][1] == "X" and map[1][1] == "X" and map[2][1] == "X":
            return True
        elif map[0][2] == "X" and map[1][2] == "X" and map[2][2] == "X":
            return True
        elif map[0][0] == "X" and map[1][1] == "X" and map[2][2] == "X":
            return True
        elif map[0][2] == "X" and map[1][1] == "X" and map[2][0] == "X":
            return True
        else:
            return False

    def o_win(map):
        if map[0][0] == "O" and map[0][1] == "O" and map[0][2] == "O":
            return True
        elif map[1][0] == "O" and map[1][1] == "O" and map[1][2] == "O":
            return True
        elif map[2][0] == "O" and map[2][1] == "O" and map[2][2] == "O":
            return True
        elif map[0][0] == "O" and map[1][0] == "O" and map[2][0] == "O":
            return True
        elif map[0][1] == "O" and map[1][1] == "O" and map[2][1] == "O":
            return True
        elif map[0][2] == "O" and map[1][2] == "O" and map[2][2] == "O":
            return True
        elif map[0][0] == "O" and map[1][1] == "O" and map[2][2] == "O":
            return True
        elif map[0][2] == "O" and map[1][1] == "O" and map[2][0] == "O":
            return True
        else:
            return False

    def tie(map):
        if map[0][0] != " " and map[0][1] != " " and map[0][2] != " " and map[1][0] != " " and map[1][1] != " " \
                                                                                                            "" and \
                map[1][2] != " " and map[2][0] != " " and map[2][1] != " " and map[2][2] != " ":
            return True

    def IntTester(prompt):
        while True:
            try:
                x = int(input(prompt))
            except ValueError:
                print("Give me a correct number!")
                continue
            if isinstance(x, int):
                return x

    def draw_map():
        map = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]
        ]
        topS = '''╔═══╦═══╦═══╗'''
        mid1S = '''║   ║   ║   ║'''
        midsS = '''╠═══╬═══╬═══╣'''
        botS = '''╚═══╩═══╩═══╝'''
        print("\n" * 30)
        print(73 * " " + (topS))
        print(73 * " " + (mid1S))
        print(73 * " " + (midsS))
        print(73 * " " + (mid1S))
        print(73 * " " + (midsS))
        print(73 * " " + (mid1S))
        print(73 * " " + (botS))
        print("\n" * 15)
        return map

    def draw(changed_map):
        top = '''╔═══╦═══╦═══╗'''
        mid1 = '''║ ''' + changed_map[0][0] + ''' ║ ''' + changed_map[0][1] + ''' ║ ''' + changed_map[0][2] + ''' ║'''
        mids = '''╠═══╬═══╬═══╣'''
        mid2 = '''║ ''' + changed_map[1][0] + ''' ║ ''' + changed_map[1][1] + ''' ║ ''' + changed_map[1][2] + ''' ║'''
        mid3 = '''║ ''' + changed_map[2][0] + ''' ║ ''' + changed_map[2][1] + ''' ║ ''' + changed_map[2][2] + ''' ║'''
        bot = '''╚═══╩═══╩═══╝'''
        print("\n" * 30)
        print(73 * " " + (top))
        print(73 * " " + (mid1))
        print(73 * " " + (mids))
        print(73 * " " + (mid2))
        print(73 * " " + (mids))
        print(73 * " " + (mid3))
        print(73 * " " + (bot))
        print("\n" * 15)
        return changed_map

    def change_x(map):
        while True:
            x_moves = []
            while True:
                y_player_x_coord = IntTester("//Numpad//"
                                             "Give me a number in 1..9: ")

                if y_player_x_coord in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                    break
                else:
                    print('Wrong number!')
                    continue
            if y_player_x_coord == 1:
                x_moves.append(0)
                x_moves.append(0)
            elif y_player_x_coord == 2:
                x_moves.append(0)
                x_moves.append(1)
            elif y_player_x_coord == 3:
                x_moves.append(0)
                x_moves.append(2)
            elif y_player_x_coord == 4:
                x_moves.append(1)
                x_moves.append(0)
            elif y_player_x_coord == 5:
                x_moves.append(1)
                x_moves.append(1)
            elif y_player_x_coord == 6:
                x_moves.append(1)
                x_moves.append(2)
            elif y_player_x_coord == 7:
                x_moves.append(2)
                x_moves.append(0)
            elif y_player_x_coord == 8:
                x_moves.append(2)
                x_moves.append(1)
            else:
                x_moves.append(2)
                x_moves.append(2)
            x = x_moves[0]
            y = x_moves[1]
            if map[x][y] == " ":
                map[x][y] = "X"
                return map
            elif map[x][y] == "O" or map[x][y] == "X":
                print("Wrong number!")
                time.sleep(2)
                continue

    def change_o(map):
        while True:
            x_moves = []
            while True:
                y_player_x_coord = IntTester("//Numpad//"
                                             "Give me a number in 1..9: ")

                if y_player_x_coord in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                    break
                else:
                    print('Wrong number!')
                    continue
            if y_player_x_coord == 1:
                x_moves.append(0)
                x_moves.append(0)
            elif y_player_x_coord == 2:
                x_moves.append(0)
                x_moves.append(1)
            elif y_player_x_coord == 3:
                x_moves.append(0)
                x_moves.append(2)
            elif y_player_x_coord == 4:
                x_moves.append(1)
                x_moves.append(0)
            elif y_player_x_coord == 5:
                x_moves.append(1)
                x_moves.append(1)
            elif y_player_x_coord == 6:
                x_moves.append(1)
                x_moves.append(2)
            elif y_player_x_coord == 7:
                x_moves.append(2)
                x_moves.append(0)
            elif y_player_x_coord == 8:
                x_moves.append(2)
                x_moves.append(1)
            else:
                x_moves.append(2)
                x_moves.append(2)
            x = x_moves[0]
            y = x_moves[1]
            if map[x][y] == " ":
                map[x][y] = "O"
                return map
            elif map[x][y] == "O" or map[x][y] == "X":
                print("Wrong number!")
                time.sleep(2)
                continue

    map = draw_map()
    for i in range(999999999):
        if i % 2 == 0:
            print("X player turn!")
            changed_map = change_x(map)
        else:
            print("O player turn!")
            changed_map = change_o(map)
        changed_map = draw(changed_map)
        if o_win(map) == True:
            print(O_win)
            replayMulti()

        elif x_win(map) == True:
            print(X_win)
            replayMulti()

        elif tie(map) == True:
            print(Draw_win)
            replayMulti()


def single_player():
    def x_win(map):
        if map[0][0] == "X" and map[0][1] == "X" and map[0][2] == "X":
            return True
        elif map[1][0] == "X" and map[1][1] == "X" and map[1][2] == "X":
            return True
        elif map[2][0] == "X" and map[2][1] == "X" and map[2][2] == "X":
            return True
        elif map[0][0] == "X" and map[1][0] == "X" and map[2][0] == "X":
            return True
        elif map[0][1] == "X" and map[1][1] == "X" and map[2][1] == "X":
            return True
        elif map[0][2] == "X" and map[1][2] == "X" and map[2][2] == "X":
            return True
        elif map[0][0] == "X" and map[1][1] == "X" and map[2][2] == "X":
            return True
        elif map[0][2] == "X" and map[1][1] == "X" and map[2][0] == "X":
            return True
        else:
            return False

    def o_win(map):
        if map[0][0] == "O" and map[0][1] == "O" and map[0][2] == "O":
            return True
        elif map[1][0] == "O" and map[1][1] == "O" and map[1][2] == "O":
            return True
        elif map[2][0] == "O" and map[2][1] == "O" and map[2][2] == "O":
            return True
        elif map[0][0] == "O" and map[1][0] == "O" and map[2][0] == "O":
            return True
        elif map[0][1] == "O" and map[1][1] == "O" and map[2][1] == "O":
            return True
        elif map[0][2] == "O" and map[1][2] == "O" and map[2][2] == "O":
            return True
        elif map[0][0] == "O" and map[1][1] == "O" and map[2][2] == "O":
            return True
        elif map[0][2] == "O" and map[1][1] == "O" and map[2][0] == "O":
            return True
        else:
            return False

    def tie(map):
        if map[0][0] != " " and map[0][1] != " " and map[0][2] != " " and map[1][0] != " " and map[1][1] != " " \
                                                                                                            "" and \
                map[1][2] != " " and map[2][0] != " " and map[2][1] != " " and map[2][2] != " ":
            return True

    def IntTester(prompt):
        while True:
            try:
                x = int(input(prompt))
            except ValueError:
                print("Give me a correct number!")
                continue
            if isinstance(x, int):
                return x

    def draw_map():
        map = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]
        ]
        topS = '''╔═══╦═══╦═══╗'''
        mid1S ='''║   ║   ║   ║'''
        midsS ='''╠═══╬═══╬═══╣'''
        botS = '''╚═══╩═══╩═══╝'''
        print("\n" * 30)
        print(73 * " " + (topS))
        print(73 * " " + (mid1S))
        print(73 * " " + (midsS))
        print(73 * " " + (mid1S))
        print(73 * " " + (midsS))
        print(73 * " " + (mid1S))
        print(73 * " " + (botS))
        print("\n" * 15)
        return map

    def draw(changed_map):
        top  = '''╔═══╦═══╦═══╗'''
        mid1 = '''║ ''' + changed_map[0][0] + ''' ║ ''' + changed_map[0][1] + ''' ║ ''' + changed_map[0][2] + ''' ║'''
        mids = '''╠═══╬═══╬═══╣'''
        mid2 = '''║ ''' + changed_map[1][0] + ''' ║ ''' + changed_map[1][1] + ''' ║ ''' + changed_map[1][2] + ''' ║'''
        mid3 = '''║ ''' + changed_map[2][0] + ''' ║ ''' + changed_map[2][1] + ''' ║ ''' + changed_map[2][2] + ''' ║'''
        bot  = '''╚═══╩═══╩═══╝'''
        print("\n" * 30)
        print(73 * " " + (top))
        print(73 * " " + (mid1))
        print(73 * " " + (mids))
        print(73 * " " + (mid2))
        print(73 * " " + (mids))
        print(73 * " " + (mid3))
        print(73 * " " + (bot))
        print("\n" * 15)
        return changed_map

    def change_x(map):
        while True:
            x_moves = []
            while True:
                y_player_x_coord = IntTester("//Numpad//"
                                             "Give me a number in 1..9: ")
                if y_player_x_coord in [ 1, 2,3,4,5,6,7,8,9]:
                    break
                else:
                    print('Wrong number!')
                    continue
            if y_player_x_coord == 1:
                x_moves.append(0)
                x_moves.append(0)
            elif y_player_x_coord == 2:
                x_moves.append(0)
                x_moves.append(1)
            elif y_player_x_coord == 3:
                x_moves.append(0)
                x_moves.append(2)
            elif y_player_x_coord == 4:
                x_moves.append(1)
                x_moves.append(0)
            elif y_player_x_coord == 5:
                x_moves.append(1)
                x_moves.append(1)
            elif y_player_x_coord == 6:
                x_moves.append(1)
                x_moves.append(2)
            elif y_player_x_coord == 7:
                x_moves.append(2)
                x_moves.append(0)
            elif y_player_x_coord == 8:
                x_moves.append(2)
                x_moves.append(1)
            else:
                x_moves.append(2)
                x_moves.append(2)


            x = x_moves[0]
            y = x_moves[1]
            if map[x][y] == " ":
                map[x][y] = "X"
                return map
            elif map[x][y] == "O" or map[x][y] == "X":
                print("Wrong number!")
                time.sleep(2)
                continue

    def change_o(map):
        while True:
            x_moves = []
            while True:
                y_player_x_coord = random.randint(1, 3) - 1
                if y_player_x_coord in [0, 1, 2]:
                    break
                else:
                    continue
            while True:
                y_player_y_coord = random.randint(1, 3) - 1
                if y_player_y_coord in [0, 1, 2]:
                    break
                else:
                    continue
            x_moves.append(y_player_x_coord)
            x_moves.append(y_player_y_coord)
            x = x_moves[0]
            y = x_moves[1]
            if map[x][y] == " ":
                map[x][y] = "O"
                return map
            elif map[x][y] == "O" or map[x][y] == "X":
                time.sleep(2)
                continue

    map = draw_map()
    for i in range(999999999):
        if i % 2 == 0:
            print("Player turn!")
            changed_map = change_x(map)
        else:
            AILoad()
            changed_map = change_o(map)
        changed_map = draw(changed_map)
        if o_win(map) == True:
            print(AI_win)
            replaySingle()
        elif x_win(map) == True:
            print(Human_win)
            replaySingle()
        elif tie(map) == True:
            print(Draw_win)
            replaySingle()


def AI_player():
    def x_win(map):
        if map[0][0] == "X" and map[0][1] == "X" and map[0][2] == "X":
            return True
        elif map[1][0] == "X" and map[1][1] == "X" and map[1][2] == "X":
            return True
        elif map[2][0] == "X" and map[2][1] == "X" and map[2][2] == "X":
            return True
        elif map[0][0] == "X" and map[1][0] == "X" and map[2][0] == "X":
            return True
        elif map[0][1] == "X" and map[1][1] == "X" and map[2][1] == "X":
            return True
        elif map[0][2] == "X" and map[1][2] == "X" and map[2][2] == "X":
            return True
        elif map[0][0] == "X" and map[1][1] == "X" and map[2][2] == "X":
            return True
        elif map[0][2] == "X" and map[1][1] == "X" and map[2][0] == "X":
            return True
        else:
            return False

    def o_win(map):
        if map[0][0] == "O" and map[0][1] == "O" and map[0][2] == "O":
            return True
        elif map[1][0] == "O" and map[1][1] == "O" and map[1][2] == "O":
            return True
        elif map[2][0] == "O" and map[2][1] == "O" and map[2][2] == "O":
            return True
        elif map[0][0] == "O" and map[1][0] == "O" and map[2][0] == "O":
            return True
        elif map[0][1] == "O" and map[1][1] == "O" and map[2][1] == "O":
            return True
        elif map[0][2] == "O" and map[1][2] == "O" and map[2][2] == "O":
            return True
        elif map[0][0] == "O" and map[1][1] == "O" and map[2][2] == "O":
            return True
        elif map[0][2] == "O" and map[1][1] == "O" and map[2][0] == "O":
            return True
        else:
            return False

    def tie(map):
        if map[0][0] != " " and map[0][1] != " " and map[0][2] != " " and map[1][0] != " " and map[1][1] != " " \
                                                                                                            "" and \
                map[1][2] != " " and map[2][0] != " " and map[2][1] != " " and map[2][2] != " ":
            return True

    def IntTester(prompt):
        while True:
            try:
                x = int(input(prompt))
            except ValueError:
                print("Give me a valid number!")
                continue
            if isinstance(x, int):
                return x

    def draw_map():
        map = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]
        ]
        map = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]
        ]
        topS = '''╔═══╦═══╦═══╗'''
        mid1S = '''║   ║   ║   ║'''
        midsS = '''╠═══╬═══╬═══╣'''
        botS = '''╚═══╩═══╩═══╝'''
        print("\n" * 30)
        print(73 * " " + (topS))
        print(73 * " " + (mid1S))
        print(73 * " " + (midsS))
        print(73 * " " + (mid1S))
        print(73 * " " + (midsS))
        print(73 * " " + (mid1S))
        print(73 * " " + (botS))
        print("\n" * 15)
        return map

    def draw(changed_map):
        top = '''╔═══╦═══╦═══╗'''
        mid1 = '''║ ''' + changed_map[0][0] + ''' ║ ''' + changed_map[0][1] + ''' ║ ''' + changed_map[0][2] + ''' ║'''
        mids = '''╠═══╬═══╬═══╣'''
        mid2 = '''║ ''' + changed_map[1][0] + ''' ║ ''' + changed_map[1][1] + ''' ║ ''' + changed_map[1][2] + ''' ║'''
        mid3 = '''║ ''' + changed_map[2][0] + ''' ║ ''' + changed_map[2][1] + ''' ║ ''' + changed_map[2][2] + ''' ║'''
        bot = '''╚═══╩═══╩═══╝'''
        print("\n" * 30)
        print(73 * " " + (top))
        print(73 * " " + (mid1))
        print(73 * " " + (mids))
        print(73 * " " + (mid2))
        print(73 * " " + (mids))
        print(73 * " " + (mid3))
        print(73 * " " + (bot))
        print("\n" * 15)
        return changed_map

    def change_x(map):
        while True:
            x_moves = []
            while True:
                y_player_x_coord = IntTester("//Numpad//"
                                             "Give me a number in 1..9: ")
                if y_player_x_coord in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                    break
                else:
                    print('Wrong number!')
                    continue
            if y_player_x_coord == 1:
                x_moves.append(0)
                x_moves.append(0)
            elif y_player_x_coord == 2:
                x_moves.append(0)
                x_moves.append(1)
            elif y_player_x_coord == 3:
                x_moves.append(0)
                x_moves.append(2)
            elif y_player_x_coord == 4:
                x_moves.append(1)
                x_moves.append(0)
            elif y_player_x_coord == 5:
                x_moves.append(1)
                x_moves.append(1)
            elif y_player_x_coord == 6:
                x_moves.append(1)
                x_moves.append(2)
            elif y_player_x_coord == 7:
                x_moves.append(2)
                x_moves.append(0)
            elif y_player_x_coord == 8:
                x_moves.append(2)
                x_moves.append(1)
            else:
                x_moves.append(2)
                x_moves.append(2)
            x = x_moves[0]
            y = x_moves[1]
            if map[x][y] == " ":
                map[x][y] = "X"
                return map
            elif map[x][y] == "O" or map[x][y] == "X":
                print("Wrong number!")
                time.sleep(2)
                continue

    def change_o(map):
        while True:
            x_moves = []
            while True:
                y_player_x_coord = random.randint(0, 2)
                if y_player_x_coord in [0, 1, 2]:
                    break
                else:
                    continue
            while True:
                y_player_y_coord = random.randint(1, 3) - 1
                if y_player_y_coord in [0, 1, 2]:
                    break
                else:
                    continue
            x_moves.append(y_player_x_coord)
            x_moves.append(y_player_y_coord)
            x = x_moves[0]
            y = x_moves[1]
            if map[x][y] == " ":
                map[x][y] = "O"
                return map
            elif map[x][y] == "O" or map[x][y] == "X":
                time.sleep(2)
                continue

    map = draw_map()
    for i in range(999999999):
        if i % 2 == 0:
            print("Player turn!")
            changed_map = change_x(map)
        else:
            AILoad()
            changed_map = change_o(map)
        changed_map = draw(changed_map)
        if o_win(map) == True:
            print(AI_win)
            replaySingle()
        elif x_win(map) == True:
            print(Human_win)
            replaySingle()
        elif tie(map) == True:
            print(Draw_win)
            replaySingle()


def spectator_player():
    def x_win(map):
        if map[0][0] == "X" and map[0][1] == "X" and map[0][2] == "X":
            return True
        elif map[1][0] == "X" and map[1][1] == "X" and map[1][2] == "X":
            return True
        elif map[2][0] == "X" and map[2][1] == "X" and map[2][2] == "X":
            return True
        elif map[0][0] == "X" and map[1][0] == "X" and map[2][0] == "X":
            return True
        elif map[0][1] == "X" and map[1][1] == "X" and map[2][1] == "X":
            return True
        elif map[0][2] == "X" and map[1][2] == "X" and map[2][2] == "X":
            return True
        elif map[0][0] == "X" and map[1][1] == "X" and map[2][2] == "X":
            return True
        elif map[0][2] == "X" and map[1][1] == "X" and map[2][0] == "X":
            return True
        else:
            return False

    def o_win(map):
        if map[0][0] == "O" and map[0][1] == "O" and map[0][2] == "O":
            return True
        elif map[1][0] == "O" and map[1][1] == "O" and map[1][2] == "O":
            return True
        elif map[2][0] == "O" and map[2][1] == "O" and map[2][2] == "O":
            return True
        elif map[0][0] == "O" and map[1][0] == "O" and map[2][0] == "O":
            return True
        elif map[0][1] == "O" and map[1][1] == "O" and map[2][1] == "O":
            return True
        elif map[0][2] == "O" and map[1][2] == "O" and map[2][2] == "O":
            return True
        elif map[0][0] == "O" and map[1][1] == "O" and map[2][2] == "O":
            return True
        elif map[0][2] == "O" and map[1][1] == "O" and map[2][0] == "O":
            return True
        else:
            return False

    def tie(map):
        if map[0][0] != " " and map[0][1] != " " and map[0][2] != " " and map[1][0] != " " and map[1][1] != " " \
                                                                                                            "" and \
                map[1][2] != " " and map[2][0] != " " and map[2][1] != " " and map[2][2] != " ":
            return True

    def IntTester(prompt):
        while True:
            try:
                x = int(input(prompt))
            except ValueError:
                print("Give me a valid number!")
                continue
            if isinstance(x, int):
                return x

    def draw_map():
        map = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]
        ]
        topS = '''╔═══╦═══╦═══╗'''
        mid1S = '''║   ║   ║   ║'''
        midsS = '''╠═══╬═══╬═══╣'''
        botS = '''╚═══╩═══╩═══╝'''
        print("\n" * 30)
        print(73 * " " + (topS))
        print(73 * " " + (mid1S))
        print(73 * " " + (midsS))
        print(73 * " " + (mid1S))
        print(73 * " " + (midsS))
        print(73 * " " + (mid1S))
        print(73 * " " + (botS))
        print("\n" * 15)
        return map

    def draw(changed_map):
        top = '''╔═══╦═══╦═══╗'''
        mid1 = '''║ ''' + changed_map[0][0] + ''' ║ ''' + changed_map[0][1] + ''' ║ ''' + changed_map[0][2] + ''' ║'''
        mids = '''╠═══╬═══╬═══╣'''
        mid2 = '''║ ''' + changed_map[1][0] + ''' ║ ''' + changed_map[1][1] + ''' ║ ''' + changed_map[1][2] + ''' ║'''
        mid3 = '''║ ''' + changed_map[2][0] + ''' ║ ''' + changed_map[2][1] + ''' ║ ''' + changed_map[2][2] + ''' ║'''
        bot = '''╚═══╩═══╩═══╝'''
        print("\n" * 30)
        print(73 * " " + (top))
        print(73 * " " + (mid1))
        print(73 * " " + (mids))
        print(73 * " " + (mid2))
        print(73 * " " + (mids))
        print(73 * " " + (mid3))
        print(73 * " " + (bot))
        print("\n" * 15)
        return changed_map

    def change_x(map):
        while True:
            x_moves = []
            while True:
                y_player_x_coord = random.randint(1, 3) - 1
                if y_player_x_coord in [0, 1, 2]:
                    break
                else:
                    continue
            while True:
                y_player_y_coord = random.randint(1, 3) - 1
                if y_player_y_coord in [0, 1, 2]:
                    break
                else:
                    continue
            x_moves.append(y_player_x_coord)
            x_moves.append(y_player_y_coord)
            x = x_moves[0]
            y = x_moves[1]
            if map[x][y] == " ":
                map[x][y] = "O"
                return map
            elif map[x][y] == "O" or map[x][y] == "X":
                time.sleep(2)
                continue

    def change_o(map):
        while True:
            x_moves = []
            while True:
                y_player_x_coord = random.randint(1, 3) - 1
                if y_player_x_coord in [0, 1, 2]:
                    break
                else:
                    continue
            while True:
                y_player_y_coord = random.randint(1, 3) - 1
                if y_player_y_coord in [0, 1, 2]:
                    break
                else:
                    continue
            x_moves.append(y_player_x_coord)
            x_moves.append(y_player_y_coord)
            x = x_moves[0]
            y = x_moves[1]
            if map[x][y] == " ":
                map[x][y] = "X"
                return map
            elif map[x][y] == "O" or map[x][y] == "X":
                continue

    map = draw_map()
    for i in range(999999999):
        if i % 2 == 0:
            AILoad()
            changed_map = change_x(map)
        else:
            AILoad()
            changed_map = change_o(map)
        changed_map = draw(changed_map)
        if o_win(map) == True:
            print(O_win)
            replaySpec()
        elif x_win(map) == True:
            print(X_win)
            replaySpec()
        elif tie(map) == True:
            print(Draw_win)
            replaySpec()

print("\n"* 8)

colorama.init()
move = 0
move_lr = 0
window_opened = False
options = ['Singleplayer', 'Multiplayer', 'Bot VS Bot', 'Exit']
options2 = ['AI(EasyBot)', 'AI(experimental)','Exit']
def submenu():
    def getKey():
        global move, move_lr, window_opened
        window_opened = False
        # 27 - esc
        # 72 - up Arrow
        # 80 - down Arrow
        # 77 - right key
        # 75 - left key
        key = ord(getch())
        if key == 27: quit()
        if key == 72:
            if window_opened != True:
                if move <= 0:
                    move = 0
                    pass
                else:
                    move -= 1
                menu(move)
        if key == 80:
            if window_opened != True:
                if move >= len(options2) - 1:
                    move = len(options2) - 1
                    pass
                else:
                    move += 1
                menu(move)
        if key == 77:
            move_lr = -1
            window_opened = True
            print_content(move)
        if key == 75:
            move_lr = 1
            window_opened = False
            menu(move)

    def menu(choice):
        os.system('cls')
        print("\n" * 10)
        print(x)
        sys.stdout.write("\033[31m\t\tHome > Singleplayer\n\033[0m")
        for i in range(len(options2)):
            if i == choice:
                sys.stdout.write('\033[36m\t  >> {}\033[0m\n'.format(options2[i]))
            else:
                print('\t   {}'.format(options2[i]))

    def print_content(choice):
        if choice == 2:
            quit("\t\tAdios!")
        elif choice == 0:
            single_player()
        elif choice == 1:
            Ai_experimental()
        move_lr = 0
    menu(move)
    while True:
        getKey()
def getKey():
    global move, move_lr, window_opened
    # 27 - esc
    # 72 - up Arrow
    # 80 - down Arrow
    # 77 - right key
    # 75 - left key
    key = ord(getch())
    if key == 27: quit()
    if key == 72:
        if window_opened != True:
            if move <= 0:
                move = 0
                pass
            else:
                move -= 1
            menu(move)
    if key == 80:
        if window_opened != True:
            if move >= len(options) - 1:
                move = len(options) - 1
                pass
            else:
                move += 1
            menu(move)
    if key == 77:
        move_lr = -1
        window_opened = True
        print_content(move)
    if key == 75:
        move_lr = 1
        window_opened = False
        menu(move)


def menu(choice):
    os.system('cls')
    print("\n" * 10)
    print(x)
    sys.stdout.write("\033[31m\t\tHome!\n\033[0m")
    for i in range(len(options)):
        if i == choice:
            sys.stdout.write('\033[36m\t  >> {}\33[0m\n'.format(options[i]))
        else:
            print('\t   {}'.format(options[i]))


def print_content(choice):
    if choice == (len(options) - 1):
        quit("\t\tAdios!")
    elif choice == (len(options) - 4):
        submenu()
    elif choice == (len(options) - 2):
        spectator_player()
    elif choice == (len(options) - 3):
        multi_player()
    move_lr = 0


menu(move)
while True:
    getKey()


