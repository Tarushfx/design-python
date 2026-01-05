from ..commons.board_base import BoardBase
class TicTacToeBoard(BoardBase):
    board = None
    __board_size = 3
    def __init__(self):
        board = ["."*self.__board_size]*self.__board_size

