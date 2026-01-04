from abc import ABC, abstractmethod


class HotDrink:
    def __init__(self, amount):
        self.amount = amount
        self.type = None

    def __str__(self) -> str:
        print(f"{type}: {self.amount} mL")


class Coffee(HotDrink):
    def __init__(self, amount):
        super().__init__(amount)
        self.type = "Coffee"


class Tea(HotDrink):
    def __init__(self, amount):
        super().__init__(amount)
        self.type = "Tea"


class Milk(HotDrink):
    def __init__(self, amount):
        super().__init__(amount)
        self.type = "Milk"
