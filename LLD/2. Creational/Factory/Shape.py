class Shape:
    def draw(self):
        pass


class Circle(Shape):
    def draw(self):
        print("Drawing a circle")


class Square(Shape):
    def draw(self):
        print("Drawing a square")


class ShapeFactory:
    def create_shape(self, shape_type):
        if shape_type == "circle":
            return Circle()
        elif shape_type == "square":
            return Square()
        else:
            raise ValueError("Invalid shape type")


if __name__ == "__main__":
    factory = ShapeFactory()

    circle = factory.create_shape("circle")
    circle.draw()

    square = factory.create_shape("square")
    square.draw()
