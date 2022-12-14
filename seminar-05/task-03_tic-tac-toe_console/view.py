import db


def request_mode_game(mode):
    """Choice a mode game."""
    print("Mode:")
    for item in mode:
        print(item)
    return int(input("--> "))


def input_name_player(name: str) -> str:
    """Input name of a player."""
    return input('Имя %s игрока -->' % (name))


def request_first_step():
    """Who is made first step?"""
    print('Кто ходит первым? 1 - игрок, 2- бот.')


def print_score_table():
    """Print to console the table score of the last players."""
    pass


def print_board(board: list):
    """Print board."""
    print('--------------')
    print('|' + board[7] + ' | ' + board[8] + ' | ' + board[9] + '|')
    print('|---+----+---|')
    print('|' + board[4] + ' | ' + board[5] + ' | ' + board[6] + '|')
    print('|---+----+---|')
    print('|' + board[1] + ' | ' + board[2] + ' | ' + board[3] + '|')
    print('--------------')

