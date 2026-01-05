from games.commons.move import Move


class TicTacToeMove(Move):
    def __init__(self, player: int, row, col) -> None:
        super().__init__(player)
        self.row = row
        self.col = col

    def set_sign(self, sign):
        self.sign = sign
