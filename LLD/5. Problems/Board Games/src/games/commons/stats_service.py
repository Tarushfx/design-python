from abc import abstractmethod, ABC
from engine.Game import Game
from games.commons.GameResult import GameResult


class StatsService(ABC):
    _instance = None
    __all_games = []

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(StatsService, cls).__new__(cls)
            cls._instance.storage = {}
        return cls._instance

    @abstractmethod
    def get_player_stats(self, player_id):
        pass

    @abstractmethod
    def get_game_stats(self, game_id):
        pass

    @classmethod
    def record_game(cls, game: GameResult):
        cls.__all_games.append(game)

    @classmethod
    def display_player_all_stats(cls, player_id):
        result = []
        for game in cls.__all_games:
            if game.id == player_id:
                result.append(game)
                print(game)
        return result
