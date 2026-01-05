def calculate_shipping_cost(weight, destination):
    if destination == "Domestic":
        if weight <= 2:
            return 5
        elif weight <= 5:
            return 10
        else:
            return 15
    elif destination == "International":
        if weight <= 1:
            return 10
        elif weight <= 3:
            return 20
        else:
            return 30
    else:
        raise ValueError("Invalid destination")


from abc import ABC, abstractmethod


class ShippingRule(ABC):
    @abstractmethod
    def is_applicable(self, weight, destination):
        pass

    @abstractmethod
    def calculate_cost(self, weight):
        pass


class DomesticRule(ShippingRule):
    def is_applicable(self, weight, destination):
        return destination == "Domestic"

    def calculate_cost(self, weight):
        if weight <= 2:
            return 5
        elif weight <= 5:
            return 10
        else:
            return 15


class InternationalRule(ShippingRule):
    def is_applicable(self, weight, destination):
        return destination == "International"

    def calculate_cost(self, weight):
        if weight <= 1:
            return 10
        elif weight <= 3:
            return 20
        else:
            return 30


def calculate_shipping_cost(weight, destination):
    for rule in [DomesticRule(), InternationalRule()]:
        if rule.is_applicable(weight, destination):
            return rule.calculate_cost(weight)
    raise ValueError("Invalid destination")
