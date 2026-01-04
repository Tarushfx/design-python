from abc import ABC, abstractmethod
from Car import *


class CarFactory(ABC):
    @abstractmethod
    def build_car(self, segment):
        pass


class LuxuryCarFactory(CarFactory):
    def build_car(self, segment, name):
        match segment:
            case CarSegments.COUPE:
                return Coupe(name)


class OrdinaryCarFactory(CarFactory):
    def build_car(self, segment, name):
        match segment:
            case CarSegments.SEDAN:
                return Sedan(name)
            case CarSegments.HATCHBACK:
                return Hatchback(name)
