from games.TTT.game import TicTacToeGame
from games.TTT.game_result import TicTacToeGameResult
from games.commons.GameResult import GameResult
from games.commons.stats_service import StatsService


class TicTacToeStats(StatsService):
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

    def record_game(self, game: TicTacToeGame):
        game_results = TicTacToeGameResult(
            winner_player=game.winner_player,
            loser_player=game.loser_player,
            id=game.id,
            players=game.get_player_list(),
        )
        self.__games.append(game_results)
        super().record_game(game_results)
        print(f"Game {game.id} recorded")
