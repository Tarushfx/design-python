# Context
class Context:
    def __init__(self):
        self.variables = {}

    def get_value(self, variable_name):
        return self.variables.get(variable_name)

    def set_value(self, variable_name, value):
        self.variables[variable_name] = value


# Abstract Expression
class Expression:
    def interpret(self, context):
        pass


# Terminal Expression
class NumberExpression(Expression):
    def __init__(self, value):
        self.value = value

    def interpret(self, context):
        return self.value


# Non-terminal Expression
class AdditionExpression(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def interpret(self, context):
        return self.left.interpret(context) + self.right.interpret(context)


# Non-terminal Expression
class SubtractionExpression(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def interpret(self, context):
        return self.left.interpret(context) - self.right.interpret(context)


# Client code
if __name__ == "__main__":
    context = Context()
    context.set_value("x", 10)
    context.set_value("y", 5)

    # Represent the expression: x + (y - 2)
    expression = AdditionExpression(
        NumberExpression(context.get_value("x")),
        SubtractionExpression(
            NumberExpression(context.get_value("y")),
            NumberExpression(2),
        ),
    )

    result = expression.interpret(context)
    print("Result:", result)  # Output: Result: 13
