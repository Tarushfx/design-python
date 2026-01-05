from abc import abstractmethod, ABC


class Game(ABC):

    def __init__(self, id):
        self.id = id
        self.__result = None
        self.__player_list = []

    def set_player_list(self, player_list):
        self.__player_list = player_list

    def get_player_list(self):
        return [p.id for p in self.__player_list]

    @abstractmethod
    def initialize(self):
        pass
