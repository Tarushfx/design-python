from games.commons.GameResult import GameResult


class TicTacToeGameResult(GameResult):
    def __str__(self):
        if not self.winner_player:
            return f"Game Result: No winner"
        return f"TicTacToeStats" \
               f": game:{self.id} x winners:{"".join(map(str, self.winner_player))}"
