from HouseBuilder import HouseBuilder


class SimpleHouseBuilder(HouseBuilder):
    def build_walls(self, wall_type="Simple walls"):
        self.house.walls = wall_type
        return self

    def build_doors(self, door_type="Simple doors"):
        self.house.doors = door_type
        return self

    def build_windows(self, window_type="Simple windows"):
        self.house.windows = window_type
        return self

    def build_roof(self, roof_type="Simple roof"):
        self.house.roof = roof_type
        return self
