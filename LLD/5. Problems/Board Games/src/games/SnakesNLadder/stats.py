from games.SnakesNLadder.game import SnakeNLadderGame
from games.SnakesNLadder.game_result import SnakesNLadderGameResult
from games.commons.stats_service import StatsService


class SnakesNLadderStats(StatsService):
    def __init__(self):
        super().__init__()
        self.__games = []

    def get_player_stats(self, player_id):
        result = []
        for game in self.__games:
            if player_id in game.players:
                result.append(game)
        return result

    def get_game_stats(self, game_id):
        result = []
        for game in self.__games:
            if game.id == game_id:
                result.append(game)
        return result

    def display_player_stats(self, player_id):
        stats = self.get_player_stats(player_id)
        for game in stats:
            print(game)

    def display_game_stats(self, game_id):
        result = self.get_game_stats(game_id)
        for game in result:
            print(game)

    def record_game(cls, game: SnakeNLadderGame):
        game_results = SnakesNLadderGameResult(
            winner_player=game.winner_player,
            loser_player=game.loser_player,
            id=game.id,
            players=game.get_player_list(),
        )
        cls.__games.append(game_results)
        super().record_game(game_results)
        print(f"Game {game.id} recorded")
