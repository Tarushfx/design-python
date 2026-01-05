from House import House
from SimpleHouse import SimpleHouseBuilder


class HouseDirector:
    def __init__(self):
        self.house = House()

    def simple_house(self):
        self.builder = SimpleHouseBuilder(self.house)
        self.builder.build_walls().build_doors()
        self.builder.build_windows().build_roof()
        return self.build()

    def build(self):
        return self.house
