from PersonBuilder import PersonBuilder


class PersonEmploymentBuilder(PersonBuilder):
    def __init__(self, person):
        super().__init__(person)

    def at(self, company):
        self.person.company = company
        return self

    def as_a(self, position):
        self.person.position = position
        return self

    def earning(self, salary):
        self.person.salary = salary
        return self
