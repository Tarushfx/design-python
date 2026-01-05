class Font:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def render(self, character):
        print(f"Rendering '{character}' in {self.name} font, size {self.size}")


class CharacterFlyweight:
    def __init__(self, char):
        self.char = char
        self.font_cache = {}  # Dictionary to cache Font objects

    def render(self, font: Font):
        if font not in self.font_cache:
            self.font_cache[font] = font  # Cache the Font object
        font_object = self.font_cache[font]
        font_object.render(self.char)


class TextEditor:
    def __init__(self):
        self.chars = []

    def add_char(self, char: str, font: Font):
        self.chars.append(CharacterFlyweight(char).render(font))


# Usage
editor = TextEditor()

bold_font = Font("Arial Bold", 12)
italic_font = Font("Times New Roman", 10)

editor.add_char("H", bold_font)
editor.add_char("e", italic_font)
editor.add_char("l", bold_font)
editor.add_char("l", bold_font)  # Reuses existing bold font object
editor.add_char("o", italic_font)
# editor.add_char(" ", None)  # No font specified
editor.add_char("W", bold_font)
editor.add_char("o", italic_font)
editor.add_char("r", bold_font)
editor.add_char("l", bold_font)  # Reuses existing bold font object

# Text editor usage would typically involve displaying the formatted text
