from enum import Enum, auto


class CarSegments(Enum):
    SEDAN = auto()
    HATCHBACK = auto()
    COUPE = auto()


class Car:
    def __init__(self, segment):
        self.wheels = 4
        self.segment = segment
        self.name = None
        self.category = None

    def __str__(self):
        return (
            f"{self.name} is a "
            f"{self.segment} "
            f"{self.category} with {self.wheels} wheels"
        )


class OrdinaryCar(Car):
    def __init__(self):
        super().__init__("Ordinary")


class Sedan(OrdinaryCar):
    def __init__(self, name):
        super().__init__()
        self.category = "Sedan"
        self.name = name


class Hatchback(OrdinaryCar):
    def __init__(self, name):
        super().__init__()
        self.category = "Hatchback"
        self.name = name


class LuxuryCar(Car):
    def __init__(self):
        super().__init__("Luxury")


class Coupe(LuxuryCar):
    def __init__(self, name):
        super().__init__()
        self.category = "Coupe"
        self.name = name
