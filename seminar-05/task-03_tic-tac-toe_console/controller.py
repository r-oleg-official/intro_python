import os
import view as v
import logic as l
import db


def start_game():
    # os.system('cls||clear') # in pycharm don't work.
    os.system('printf "\033[2J"')   # clear console PyCharm
    mode_game = v.request_mode_game(db.mode)
    match mode_game:
        case 1:
            name_player_1 = v.input_name_player('первого')
            name_player_2 = v.input_name_player('второго')
        case 2:
            print('Данный режим в разработке.')
            exit(0)
            # name_player_1 = v.input_name_player('')
            # name_player_2 = 'Бот'
        case 3:
            print('Данный режим в разработке.')
            exit(0)
            # name_player_1 = 'Бот-1'
            # name_player_2 = 'Бот-2'
        case 4:
            exit(0)
        case 5:
            print(len(db.new_board))
            exit(0)

    print(name_player_1, name_player_2)
    v.print_board(db.new_board)

