from enum import Enum
from math import cos, sin, pi


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x},{self.y})"


class CartesianPoint(Point):
    def __init__(self, x, y):
        super().__init__(x, y)


class PolarPoint(Point):
    def __init__(self, rho, theta):
        super().__init__(rho * cos(theta), rho * sin(theta))


class PointType(Enum):
    CARTESIAN = 1
    POLAR = 2


class PointFactory:
    @staticmethod
    def new_point(type=PointType.CARTESIAN, x=0, y=0):
        match type:
            case PointType.CARTESIAN:
                return CartesianPoint(x, y)
            case PointType.POLAR:
                return PolarPoint(x, y)


if __name__ == "__main__":
    pf = PointFactory()
    p = pf.new_point(PointType.CARTESIAN, 1, 1)
    print(p)

    p = pf.new_point(PointType.POLAR, 1, 1)
    print(p)

    p = pf.new_point(PointType.POLAR, 1, pi)
    print(p)
