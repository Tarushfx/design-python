class Person:
    def __init__(self):
        # address
        self.street = None
        self.city = None
        self.state = None
        self.zipcode = None
        # employment
        self.company = None
        self.position = None
        self.salary = None

    def __str__(self) -> str:
        return (
            f"Address: {self.street} {self.city} {self.state} {self.zipcode}\n"
            + f"Employed at: {self.company} {self.position} {self.salary}"
        )
