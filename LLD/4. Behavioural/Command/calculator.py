# Command Interface
class Command:
    def execute(self):
        pass

    def undo(self):
        pass


# Concrete Commands
class AddCommand(Command):
    def __init__(self, calculator, value):
        self.calculator = calculator
        self.value = value

    def execute(self):
        self.calculator.add(self.value)

    def undo(self):
        self.calculator.subtract(self.value)


class SubtractCommand(Command):
    def __init__(self, calculator, value):
        self.calculator = calculator
        self.value = value

    def execute(self):
        self.calculator.subtract(self.value)

    def undo(self):
        self.calculator.add(self.value)


class Calculator:
    def __init__(self):
        self.current_value = 0

    def add(self, value):
        self.current_value += value

    def subtract(self, value):
        self.current_value -= value


# Invoker
class Invoker:
    def __init__(self):
        self.history = []

    def execute_command(self, command):
        command.execute()
        self.history.append(command)

    def undo_last_command(self):
        if self.history:
            last_command = self.history.pop()
            last_command.undo()


calculator = Calculator()
invoker = Invoker()

add_command = AddCommand(calculator, 5)
invoker.execute_command(add_command)
invoker.execute_command(add_command)

subtract_command = SubtractCommand(calculator, 3)
invoker.execute_command(subtract_command)

print(calculator.current_value)
invoker.undo_last_command()
invoker.undo_last_command()

print(calculator.current_value)
