"""Создайте программу для игры с конфетами человек против человека.
Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
a) Добавьте игру против бота
b) Подумайте как наделить бота ""интеллектом""
"""
import os
from random import randint


def request_mode_game(mode):
    """Choice a mode game."""
    print(" ------------------------")
    print("| Mode:                |")
    for item in mode:
        print(item)
    print(" ------------------------")
    return int(input("--> "))


def input_name_player(name: str) -> str:
    """Input name of a player."""
    return input("Имя %s игрока -->" % name)


def draw_board(board: list, player1: str, player2: str):
    """Drawing the board."""
    # for i in range(3):
    #     if len(board[i]) < 4:
    #         for j in range(4 - len(board[i])):
    #             board[i] = " " + board[i]
    print("  ---------------------------")
    print(f'| Счет игрока {player1}: \t{str(board[0])} |')
    print("  ---------------------------")
    print(f'| Счет игрока {player2}: \t{str(board[1])} |')
    print("  ---------------------------")
    print(f'| Осталось конфет: \t{str(board[2])} |')
    print("  ---------------------------")


def print_step(name_player: str):
    print()
    print(f'Ход за {name_player}.')


def print_winner(name_player: str):
    # os.system('cls||clear')  # in pycharm don't work.
    os.system('printf "\033[2J"')  # clear console PyCharm
    print("-----------------------")
    print(f'Победитель {name_player}!!!')
    print("-----------------------")


def first_step() -> int:
    choice = randint(1, 2)
    if choice == 0:
        return 1
    else:
        return 2


def step_player(board: list, step: int) -> int:
    tmp = step
    if board[2] < step: tmp = board[2]
    count = input(f'Взять конфет (1 - {tmp}): ')
    while (int(count) < 1) or (int(count) > tmp):
        count = input(f'Ошибка! Взять можно до {tmp} конфет:')
    return int(count)


def step_bot_norm(board: list, step: int) -> int:
    if board[2] > step:
        return randint(1, step)
    return randint(1, board[2])


def step_bot_hard(board: list, step: int) -> int:
    if (board[2] // step) < 3: return board[2] - step - 1
    if board[2] > step:
        return randint(1, step)
    return randint(1, board[2])


def start_game(player1: str, player2: str, candy: int, mode_bot: int):
    # [0] - player-1, [1] - player-2, [2] - score
    board = [0, 0, candy]
    draw_board(board, player1, player2)
    who = first_step()
    in_game = True

    while in_game:
        match who:
            case 1:
                # Step player-1
                if 'Бот' not in player1:
                    print_step(player1)
                    board[0] += step_player(board, max_step)
                if 'Бот' in player1:
                    if mode_bot == 1:
                        board[0] += step_bot_norm(board, max_step)
                    if mode_bot == 2:
                        board[0] += step_bot_hard(board, max_step)
                board[2] -= board[0]
                if board[2] <= 1:
                    draw_board(board, player1, player2)
                    print_winner(player1)
                    # in_game = False
                    return
                who = 2

            case 2:
                # Step player-2
                if 'Бот' not in player2:
                    print_step(player2)
                    board[1] += step_player(board, max_step)
                if 'Бот' in player2:
                    if mode_bot == 1:
                        board[1] += step_bot_norm(board, max_step)
                    if mode_bot == 2:
                        board[1] += step_bot_hard(board, max_step)
                board[2] -= board[1]
                if board[2] <= 1:
                    draw_board(board, player1, player2)
                    print_winner(player2)
                    #in_game = False
                    return
                who = 1
        draw_board(board, player1, player2)
    return


def controller():
    # os.system('cls||clear')  # in pycharm don't work.
    os.system('printf "\033[2J"')  # clear console PyCharm
    print(" -----------------------")
    print(f'| Игра {candy} конфета(ы). |')
    print(" -----------------------")

    mode_game = request_mode_game(mode)
    match mode_game:
        case 1:
            # Player vs Player
            # os.system('cls||clear')  # in pycharm don't work.
            os.system('printf "\033[2J"')  # clear console PyCharm
            name_player1 = input_name_player('первого')
            name_player2 = input_name_player('второго')
            start_game(name_player1, name_player2, candy, 0)
        case 2:
            # Player vs PC. Normal
            # os.system('cls||clear')  # in pycharm don't work.
            os.system('printf "\033[2J"')  # clear console PyCharm
            name_player = input_name_player('')
            start_game(name_player, 'Бот', candy, 1)
        case 3:
            # Player vs PC. Hard
            # os.system('cls||clear')  # in pycharm don't work.
            os.system('printf "\033[2J"')  # clear console PyCharm
            name_player = input_name_player('')
            start_game(name_player, 'Бот', candy, 2)
        case _:
            exit(0)


def main():
    controller()


mode = ['| 1 - Player vs Player   |', '| 2 - Player vs PC(Norm) |', '| 3 - Player vs PC(Hard) |',
        '| 4 - Exit game          |']
candy = int(100)  # a numbers of candies in the game.
max_step = int(28)  # a maximum number to get candy once time.

if __name__ == '__main__':
    main()
