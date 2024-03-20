from abc import abstractmethod


# TODO:  re-studty this
class Color:
    """Represents a color with its RGB values."""

    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue

    def __str__(self):
        return f"RGB({self.red}, {self.green}, {self.blue})"


class ColorFactory:
    """Factory class that creates and stores Color objects (flyweights)."""

    color_cache = {}  # Dictionary to cache Color objects

    def __new__(cls, *args):
        """Singleton pattern to ensure a single instance of ColorFactory."""
        if not hasattr(cls, "instance"):
            cls.instance = super().__new__(cls)
        return cls.instance

    def get_color(self, red, green, blue):
        """Retrieves a Color object from the cache or creates a new one."""
        color_key = (red, green, blue)
        if color_key not in self.color_cache:
            self.color_cache[color_key] = Color(red, green, blue)
        return self.color_cache[color_key]


class Shape:
    """Abstract base class representing a shape."""

    def __init__(self, color):
        self.color = color

    @abstractmethod
    def draw(self):
        """Abstract method for drawing the shape (implementation depends on specific shape)."""
        pass


class Circle(Shape):
    """Concrete class representing a circle."""

    def __init__(self, color, x, y, radius):
        super().__init__(color)
        self.x = x
        self.y = y
        self.radius = radius

    def draw(self):
        print(
            f"Drawing a circle at ({self.x}, {self.y}) "
            + f"with radius {self.radius} in color {self.color}"
        )


class Rectangle(Shape):
    """Concrete class representing a rectangle."""

    def __init__(self, color, x, y, width, height):
        super().__init__(color)
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self):
        print(
            f"Drawing a rectangle at ({self.x}, {self.y}) with width {self.width} and height {self.height} in color {self.color}"
        )


# Usage
color_factory = ColorFactory()  # Singleton instance

red = color_factory.get_color(255, 0, 0)
green = color_factory.get_color(0, 255, 0)
blue = color_factory.get_color(0, 0, 255)

circle1 = Circle(red, 10, 10, 5)
circle2 = Circle(green, 50, 50, 3)
rectangle = Rectangle(blue, 20, 20, 30, 40)

circle1.draw()
circle2.draw()
rectangle.draw()

# Notice that even though multiple circles and the rectangle have different colors,
# only three Color objects were created and stored in the cache by the ColorFactory.
