from abc import ABC, abstractmethod


class GameManager(ABC):
    id = None
    game = None
    max_players = 2
    min_players = 2
    players = None
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(GameManager, cls).__new__(cls)
        return cls._instance

    def __init__(self, id):
        self.id = id
        self.players = []

    def set_game(self, game):
        self.game = game

    @abstractmethod
    def set_players(self, players):
        pass

    @abstractmethod
    def add_player(self, player):
        pass

    @abstractmethod
    def move(self, move):
        pass
