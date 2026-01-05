from abc import abstractmethod


class Game(object):
    __player_list = None
    __result = None
    id = None

    def __init__(self, id):
        self.id = id

    def set_player_list(self, player_list):
        self.__player_list = player_list

    def get_player_list(self):
        return [p.id for p in self.__player_list]

    @abstractmethod
    def initialize(self):
        pass
