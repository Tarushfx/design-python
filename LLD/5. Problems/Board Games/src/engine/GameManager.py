from abc import ABC, abstractmethod


class GameManager(ABC):
    game = None
    __max_players = 2
    __min_players = 2

    def __init__(self, game):
        self.game = game

    @abstractmethod
    def set_players(self, players):
        pass

    @abstractmethod
    def move(self, move):
        pass
