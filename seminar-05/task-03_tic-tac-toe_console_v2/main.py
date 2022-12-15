import os
from random import randint
from random import choice


# View
def request_mode_game(mode):
    """Choice a mode game."""
    print(" ----------------------")
    print("| Mode:                |")
    for item in mode:
        print(item)
    print(" ----------------------")
    return int(input("--> "))


def input_name_player(name: str) -> str:
    """Input name of a player."""
    return input("Имя %s игрока -->" % name)


def choice_letter(player1: str, player2: str) -> list:
    """Player is choice of a letter: X or O."""
    letter = ''
    if 'Бот' in player1 and 'Бот' in player2:
        return ['X', 'O']
    while not (letter == 'X' or letter == 'O'):
        print(" ------------------------------------------")
        print("| Ввод на английской раскладке клавиатуры. |")
        print(" ------------------------------------------")
        letter = input("Выберете Х, или О для первого игрока --> ").upper()
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']


def draw_board(board: list):
    """Print board."""
    # os.system('cls||clear')  # in pycharm don't work.
    os.system('printf "\033[2J"')  # clear console PyCharm
    print('-------------')
    print('| ' + board[7] + ' | ' + board[8] + ' | ' + board[9] + ' |')
    print('|---+---+---|')
    print('| ' + board[4] + ' | ' + board[5] + ' | ' + board[6] + ' |')
    print('|---+---+---|')
    print('| ' + board[1] + ' | ' + board[2] + ' | ' + board[3] + ' |')
    print('-------------')


# Database
mode = ['| 2 - Player vs PC     |', '| 4 - Exit game        |']
mode2 = ['| 1 - Player vs Player |', '| 2 - Player vs PC     |', '| 3 - PC vs PC         |', '| 4 - Exit game        |']

# Winner's combo
#            0      1      2      3      4      5      6      7      8      9
board_1 = ['   ', ' X ', '   ', '   ', '   ', ' X ', '   ', '   ', '   ', ' X ']
board_2 = ['   ', '   ', '   ', ' X ', '   ', ' X ', '   ', ' X ', '   ', '   ']
board_3 = ['   ', ' X ', ' X ', ' X ', '   ', '   ', '   ', '   ', '   ', '   ']
board_4 = ['   ', '   ', '   ', '   ', ' X ', ' X ', ' X ', '   ', '   ', '   ']
board_5 = ['   ', '   ', '   ', '   ', '   ', '   ', '   ', ' X ', ' X ', ' X ']
board_6 = ['   ', ' X ', '   ', '   ', ' X ', '   ', '   ', ' X ', '   ', '   ']
board_7 = ['   ', '   ', ' X ', '   ', '   ', ' X ', '   ', '   ', ' X ', '   ']
board_8 = ['   ', '   ', '   ', ' X ', '   ', '   ', ' X ', '   ', '   ', ' X ']


# Logic
def request_first_step(player1: str, player2: str) -> str:
    """Who is made first step?"""
    if player1 == 'Бот':
        player1 = 'Бот-1'
    elif player2 == 'Бот':
        player2 = 'Бот-2'

    print(f'Кто ходит первым: {player1}, или {player2}?')
    if randint(0, 1) == 0: return player2
    return player1


def made_step(board: list, letter: str, cell: int):
    """Done step."""
    board[cell] = letter


def is_winner(board: list, letter: str) -> bool:
    """Check player is the winner?"""
    return ((board[1] == letter and board[5] == letter and board[9] == letter) or
            (board[3] == letter and board[5] == letter and board[7] == letter) or
            (board[1] == letter and board[2] == letter and board[3] == letter) or
            (board[4] == letter and board[5] == letter and board[6] == letter) or
            (board[7] == letter and board[8] == letter and board[9] == letter) or
            (board[1] == letter and board[4] == letter and board[7] == letter) or
            (board[2] == letter and board[5] == letter and board[8] == letter) or
            (board[3] == letter and board[6] == letter and board[9] == letter))


def copy_board_bot(board: list) -> list:
    """Copy board for calc step of the bot."""
    return board.copy()


def is_cell_free(board: list, cell: int) -> bool:
    """Check step. Cell is a free?"""
    return board[cell] == ' '


def step_player(board: list) -> int:
    """Player is input next step."""
    cell = ''
    while cell not in '1 2 3 4 5 6 7 8 9'.split() or not is_cell_free(board, int(cell)):
        cell = input("Введите номер клетки (1-9) --> ")
    return int(cell)


def random_step_bot(board: list, steps_li: list) -> int:
    """Random step by bot."""
    variable_li = []
    for item in steps_li:
        if is_cell_free(board, item):
            variable_li.append(item)

    if len(variable_li) > 0:
        return choice(variable_li)
    else:
        return None


def step_bot(board: list, bot_letter: str) -> str:
    """Brain of the bot."""
    # Definition of a bot's letter
    if bot_letter == 'X':
        player_letter = 'O'
    else:
        player_letter = 'X'

    # Definition: will the bot win if it takes the next step?
    for i in range(1, 10):
        dub_board = copy_board_bot(board)
        if is_cell_free(dub_board, i):
            made_step(dub_board, bot_letter, i)
            if is_winner(dub_board, bot_letter): return i

    # Definition: will the player win if it takes the next step? If True => blocked it.
    for i in range(1, 10):
        dub_board = copy_board_bot(board)
        if is_cell_free(dub_board, i):
            made_step(dub_board, player_letter, i)
            if is_winner(dub_board, player_letter):
                return i

    # Angles check
    move = random_step_bot(board, [1, 3, 7, 9])
    if move is not None: return move

    # Center check
    if is_cell_free(board, 5): return 5

    # Made step to one side
    return random_step_bot(board, [2, 4, 6, 8])


def is_finish_him(board: list) -> bool:
    """Check is filling the board. If the cell full is True."""
    for i in range(1, 10):
        if is_cell_free(board, i):
            return False
    return True


def mortal_kombat_begin(player1: str, player2: str):
    """Run new game."""
    while True:
        game_board = [' '] * 10
        player1_letter, player2_letter = choice_letter(player1, player2)
        who = request_first_step(player1, player2)
        print(f' {who} ходит первым.')
        mortal_kombat = True

        while mortal_kombat:
            if who == player1:
                # Step player-1
                draw_board(game_board)
                step = step_player(game_board)
                made_step(game_board, player1_letter, step)

                if is_winner(game_board, player1_letter):
                    draw_board(game_board)
                    print(f'{player1}, победил!')
                    mortal_kombat = False
                else:
                    if is_finish_him(game_board):
                        draw_board(game_board)
                        print("Ничья!")
                        break
                    else:
                        who = player2
            else:
                # Step player-2
                step = step_bot(game_board, player2_letter)
                made_step(game_board, player2_letter, step)

                if is_winner(game_board, player2_letter):
                    draw_board(game_board)
                    print(f'{player2}, победил!')
                    mortal_kombat = False
                else:
                    if is_finish_him(game_board):
                        draw_board(game_board)
                        print("Ничья!")
                        break
                    else:
                        who = player1
        print("Сыграем ещё раз? (y/n)")
        if not input().lower().startswith('y'):
            break


# Controller
def cont():
    # os.system('cls||clear')  # in pycharm don't work.
    os.system('printf "\033[2J"')  # clear console PyCharm
    print(" -------------------------")
    print("| Игра в крестики-нолики. |")
    print(" -------------------------")
    mode_game = request_mode_game(mode)
    match mode_game:
        case 1:
            # Player vs Player
            print('Данный режим в разработке.\nНужна логика смены поля между игроками.')
            exit(0)
            # os.system('cls||clear')  # in pycharm don't work.
            os.system('printf "\033[2J"')  # clear console PyCharm
            name_player_1 = input_name_player('первого')
            name_player_2 = input_name_player('второго')
            mortal_kombat_begin(name_player_1, name_player_2)
        case 2:
            # Player vs PC
            # os.system('cls||clear')  # in pycharm don't work.
            os.system('printf "\033[2J"')  # clear console PyCharm
            name_player = input_name_player('')
            mortal_kombat_begin(name_player, 'Бот')
        case 3:
            # Bot vs Bot
            mortal_kombat_begin('Бот-1', 'Бот-2')
        case 4:
            exit(0)


def main():
    cont()


if __name__ == "__main__":
    main()
