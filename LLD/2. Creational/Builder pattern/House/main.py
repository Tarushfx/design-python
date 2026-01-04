from HouseDirector import HouseDirector
from SimpleHouse import SimpleHouseBuilder


if __name__ == "__main__":
    director = HouseDirector()
    house = director.simple_house()
    print(house)
