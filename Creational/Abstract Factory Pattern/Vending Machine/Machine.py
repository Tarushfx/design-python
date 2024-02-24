from abc import ABC
from enum import Enum, auto
from Factory import *


class AvailableDrinks(Enum):
    COFFEE = auto()
    TEA = auto()
    MILK = auto()


class Machine:

    def __init__(self):
        self.factories = []
        # self.instantiated = False

        for drinks in AvailableDrinks:
            print(drinks, drinks.name)
            className = drinks.name.capitalize()
            self.factories.append(eval(className + "Factory")())
        # print(self.factories)

    def make_drink(self):
        print("What would you like:\n")
        for idx, drinks in enumerate(AvailableDrinks):
            print(f"{idx}: {drinks.name}")
        idx = int(input())
        amount = int(input("Enter the amount: "))
        self.factories[idx].prepare(amount)
