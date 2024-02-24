from Person import Person
from PersonDirector import PersonBuilderDirector

if __name__ == "__main__":
    person = Person()
    director = PersonBuilderDirector(person)
    director.lives.in_city("New York").in_state("NY").in_pincode("10001").at(
        "123 Main St"
    )
    director.works.at("Uberland").as_a("software engineer").earning("100k")
    director.works.at("Google")
    person = director.build()
    print(person)
