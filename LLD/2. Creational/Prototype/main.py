from abc import ABC, abstractmethod


class Document(ABC):
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def __str__(self):
        return f"Title: {self.title}\nContent: {self.content}"

    @abstractmethod
    def clone(self):
        pass


class TextDocument(Document):
    def __init__(self, title, content, font_size):
        super().__init__(title, content)
        self.font_size = font_size

    def clone(self):
        return TextDocument(self.title, self.content, self.font_size)


class SpreadsheetDocument(Document):
    def __init__(self, title, content, rows, columns):
        super().__init__(title, content)
        self.rows = rows
        self.columns = columns

    def clone(self):
        return SpreadsheetDocument(self.title, self.content, self.rows, self.columns)
