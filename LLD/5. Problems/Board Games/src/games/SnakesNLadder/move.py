from games.commons.move import Move


class SnakeNLadderMove(Move):
    def __init__(self, player: int, val) -> None:
        super().__init__(player)
        self.roll = val

    def set_sign(self, sign):
        self.sign = sign
