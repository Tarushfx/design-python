from games.commons.GameResult import GameResult


class TicTacToeGameResult(GameResult):
    def __str__(self):
        return f"TicTacToeStats" \
               f": game:{self.id} x winners:{"".join(map(str, self.winner_player))}"
