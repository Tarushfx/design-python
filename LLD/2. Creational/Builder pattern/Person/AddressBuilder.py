from PersonBuilder import PersonBuilder


class PersonAddressBuilder(PersonBuilder):
    def __init__(self, person):
        super().__init__(person)

    def at(self, address):
        self.person.street = address
        return self

    def in_city(self, city):
        self.person.city = city
        return self

    def in_state(self, state):
        self.person.state = state
        return self

    def in_pincode(self, pin):
        self.person.zipcode = pin
        return self
