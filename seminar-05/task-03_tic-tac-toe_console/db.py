def read_score_db():
    """Read score a last games."""
    pass


def write_score_db():
    """Write table a score of the players to a table: place, name, time game"""
    pass


def logger():
    """Write time of a start and end game."""
    pass


mode = ['1 - Player vs Player', '2 - Player vs PC', '3 - PC vs PC', '4 - Exit game']
new_board = ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ']

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

