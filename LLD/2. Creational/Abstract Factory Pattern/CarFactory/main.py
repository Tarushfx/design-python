from CarFactory import *

if __name__ == "__main__":
    lcf = LuxuryCarFactory()
    ocf = OrdinaryCarFactory()
    c1 = lcf.build_car(CarSegments.COUPE, "Tesla")
    c2 = ocf.build_car(CarSegments.SEDAN, "Honda city")
    c3 = ocf.build_car(CarSegments.HATCHBACK, "Tata Altroz")

    # print(dir(c1))
    print(c1)
    print(c2)
    print(c3)
