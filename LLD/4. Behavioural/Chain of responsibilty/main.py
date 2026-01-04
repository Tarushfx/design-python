class Handler:
    def __init__(self, successor=None):
        self._successor = successor

    def handle_request(self, expense):
        pass

    def __str__(self) -> str:
        return self.name


class Manager(Handler):
    def __init__(self, name, approval_limit, successor=None):
        super().__init__(successor)
        self.name = name
        self.approval_limit = approval_limit

    def handle_request(self, expense):
        if expense.amount <= self.approval_limit:
            print(f"{self.name} approved the expense of ${expense.amount}")
            return
        if self._successor:
            print(f"Request transferred to {self._successor}.")
            self._successor.handle_request(expense)
            return
        print(f"Request has been rejected.")


class Expense:
    def __init__(self, amount):
        self.amount = amount


# Usage
P = Manager("President", 300)
VP = Manager("Vice President", 200, P)
employee = Manager("Employee", 100, VP)

expense1 = Expense(50)
expense2 = Expense(150)
expense3 = Expense(250)
expense4 = Expense(350)

employee.handle_request(expense1)
print()
employee.handle_request(expense2)
print()
employee.handle_request(expense3)
print()
employee.handle_request(expense4)
