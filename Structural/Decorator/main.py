class Pizza:
    def __init__(self):
        self.description = "Basic pizza"
        self.price = 5

    def get_description(self):
        return self.description

    def get_price(self):
        return self.price

    def __str__(self) -> str:
        return f"Description: {self.description},"\
            +f" Price: ${self.price}"


# Decorators (inherit from base Pizza class)
class Mozzarella(Pizza):
    def __init__(self, pizza):
        super().__init__()
        self.pizza = pizza
        self.description = self.pizza.get_description() + \
            " with mozzarella cheese"
        self.price += 1


class TomatoSauce(Pizza):
    def __init__(self, pizza):
        super().__init__()
        self.pizza = pizza
        self.description = self.pizza.get_description() + \
            " with tomato sauce"
        self.price += 1


class Pepperoni(Pizza):
    def __init__(self, pizza):
        super().__init__()
        self.pizza = pizza
        self.description = self.pizza.get_description() + \
            " with pepperoni"
        self.price += 2


# Usage: Create a basic pizza and add toppings dynamically
if __name__ == "__main__":

    pizza = Pizza()
    print(pizza)
    mozzarella_pizza = Mozzarella(pizza)
    print(mozzarella_pizza)
    tomato_sauce_pizza = TomatoSauce(mozzarella_pizza)
    print(tomato_sauce_pizza)
    pepperoni_pizza = Pepperoni(tomato_sauce_pizza)
    print(pepperoni_pizza)
