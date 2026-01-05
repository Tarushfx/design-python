from games.commons.board_base import BoardBase


class TicTacToeBoard(BoardBase):
    board = None

    def __init__(self):
        self.__board_size = 3
        self.board = [["."] * self.__board_size for _ in range(self.__board_size)]

    def is_position_filled(self, row, col):
        if not (0 <= row < self.__board_size and 0 <= col < self.__board_size):
            return False
        if self.board[row][col] != ".":
            return True
        return False

    def get_position(self, row, col):
        if self.is_position_filled(row, col):
            return self.board[row][col]
        return None

    def place(self, row, col, sign):
        self.board[row][col] = sign

    def print_board(self):
        print(f"Printing Board")
        for row in self.board:
            print(row)

    def size(self):
        return self.__board_size
