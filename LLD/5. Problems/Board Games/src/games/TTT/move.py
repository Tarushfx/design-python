from games.commons.move import Move


class TicTacToeMove(Move):
    def __init__(self, player: int, row, col, sign) -> None:
        super().__init__(player)
        self.player = player
        self.row = row
        self.col = col
        self.sign = sign
