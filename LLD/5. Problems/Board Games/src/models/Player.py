from abc import ABC


class Player(ABC):
    id = None
    __history = []

    def __init__(self, id: int, name: str):
        self.id = id
        self.__history = []
        self.name = name
