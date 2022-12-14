import os
from random import randint


# View
def request_mode_game(mode):
    """Choice a mode game."""
    print("Mode:")
    for item in mode:
        print(item)
    return int(input("--> "))


def input_name_player(name: str) -> str:
    """Input name of a player."""
    return input("Имя %s игрока -->" % (name))


def choice_letter() -> list:
    """Player is choice of a letter: X or O."""
    letter = ''
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
    print('-------------')
    print('|' + board[7] + '|' + board[8] + '|' + board[9] + '|')
    print('|---+---+---|')
    print('|' + board[4] + '|' + board[5] + '|' + board[6] + '|')
    print('|---+---+---|')
    print('|' + board[1] + '|' + board[2] + '|' + board[3] + '|')
    print('-------------')


# Database
mode = ['1 - Player vs Player', '2 - Player vs PC', '3 - PC vs PC', '4 - Exit game']
#              0      1      2      3      4      5      6      7      8      9
new_board = ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ']

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
def request_first_step():
    """Who is made first step?"""
    print('Кто ходит первым, Игрок, или Бот?')
    return randint(0, 1)


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


# Controller
def cont():
    # os.system('cls||clear') # in pycharm don't work.
    os.system('printf "\033[2J"')  # clear console PyCharm
    mode_game = request_mode_game(mode)
    match mode_game:
        case 1:
            os.system('printf "\033[2J"')
            name_player_1 = input_name_player('первого')
            name_player_2 = input_name_player('второго')
            letters = choice_letter()
            first_step = request_first_step()  # 0 - man, 1 - bot
        case 2:
            print('Данный режим в разработке.')
            exit(0)
            name_player_1 = input_name_player('')
            name_player_2 = 'Бот'
            letters = choice_letter()
            first_step = request_first_step()  # 0 - man, 1 - bot
        case 3:
            print('Данный режим в разработке.')
            exit(0)
            name_player_1 = 'Бот-1'
            name_player_2 = 'Бот-2'
        case 4:
            exit(0)
        case 5:
            print(choice_letter())
            exit(0)

    # draw_board(new_board)
    # draw_board(board_1)


def main():
    cont()


if __name__ == "__main__":
    main()
