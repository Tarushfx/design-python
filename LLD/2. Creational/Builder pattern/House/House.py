# house.py
class House:
    def __init__(self):
        self.walls = None
        self.doors = None
        self.windows = None
        self.roof = None

    def __str__(self):
        return (
            f"House(walls={self.walls}, doors={self.doors},"
            + f" windows={self.windows}, roof={self.roof})"
        )
