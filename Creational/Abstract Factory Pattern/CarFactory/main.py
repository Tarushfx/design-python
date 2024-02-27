from CarFactory import *

if __name__ == "__main__":
    lcf = LuxuryCarFactory()
    ocf = OrdinaryCarFactory()
    c1 = lcf.build_car(CarSegments.COUPE, "Tesla")
    c2 = ocf.build_car(CarSegments.SEDAN, "Honda city")

    # print(dir(c1))
    print(c1)
    print(c2)
