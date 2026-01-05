class Car:
    def __init__(self):
        self.wheels = None
        self.doors = None
        self.engine = None

    def __str__(self) -> str:
        return f"Engine: {self.engine} \nWheels: {self.wheels}\nDoors: {self.doors}"


class CarBuilder:
    def __init__(self):
        self.car = None

    def build(self):
        return self.car


class EngineBuilder(CarBuilder):
    def buildEngine(self):
        self.car.engine = "v6 engine"
        return self


class DoorsBuilder(EngineBuilder):
    def buildDoor(self):
        self.car.doors = 4
        return self


class WheelBuilder(DoorsBuilder):
    def buildWheels(self):
        self.car.wheels = 4
        return self


class CarBorn(WheelBuilder):
    def born(self, car=Car()):
        self.car = car
        return self


if __name__ == "__main__":
    # The CarBorn object is only propagating throughout
    # hence it is interchangeable throughout
    car = CarBorn().born()
    print(car, dir(car)[-6:])
    car = car.buildDoor()
    print(car, dir(car)[-6:])
    car = car.buildWheels()
    print(car, dir(car)[-6:])
    car = car.buildEngine()
    print(car, dir(car)[-6:])
    car = car.build()
    print(car)
