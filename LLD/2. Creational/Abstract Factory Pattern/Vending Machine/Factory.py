from abc import ABC, abstractmethod
from HotDrink import *


class HotDrinkFactory(ABC):
    def __init__(self, amount):
        self.amount = amount

    @abstractmethod
    def prepare(self, amount):
        pass


class CoffeeFactory(ABC):
    def prepare(self, amount):
        self.instructions = (
            "1) Grind coffee beans.\n2) Boil water.\n"
            + f"3) Pour {amount} mL water and add coffee.\n4) Enjoy."
        )
        print(self.instructions)
        return Coffee(amount)


class TeaFactory(ABC):
    def prepare(self, amount):
        self.instructions = (
            "1) Boil water.\n"
            + f"2) Pour {amount} mL water and add tea.\n"
            + "3) Enjoy."
        )
        print(self.instructions)
        return Tea(amount)


class MilkFactory(ABC):

    def prepare(self, amount):
        self.amount = amount
        self.instructions = (
            "1) Boil Milk.\n" + f"2) Pour {amount} mL milk.\n" + "3) Enjoy."
        )
        print(self.instructions)
        return Milk(amount)
