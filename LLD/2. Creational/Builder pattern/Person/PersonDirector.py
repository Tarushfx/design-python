from AddressBuilder import PersonAddressBuilder
from EmploymentBuilder import PersonEmploymentBuilder


class PersonBuilderDirector:
    def __init__(self, person):
        self.person = person

    @property
    def lives(self):
        return PersonAddressBuilder(self.person)

    @property
    def works(self):
        return PersonEmploymentBuilder(self.person)

    def build(self):
        return self.person
