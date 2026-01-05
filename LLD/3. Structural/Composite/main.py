from abc import abstractmethod


class Component:
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def get_size(self):
        """Abstract method for calculating size (optional)."""
        pass

    @abstractmethod
    def list(self, indent):
        pass


class File(Component):
    def __init__(self, name, size):
        super().__init__(name)
        self.size = size

    def get_size(self):
        return self.size

    def list(self, indent):
        print("-" * indent + f"{self.name} {self.get_size()} (file)")


class Folder(Component):
    def __init__(self, name):
        super().__init__(name)
        self.children = []

    def add(self, component):
        self.children.append(component)

    def remove(self, component):
        self.children.remove(component)

    def get_size(self):
        total_size = 0
        for child in self.children:
            total_size += child.get_size()
        return total_size

    def list(self, indent=0):

        print("-" * indent + f"{self.name} {self.get_size()} (folder)")
        for child in self.children:
            child.list(indent + 1)


# Usage
root = Folder("root")

documents = Folder("Documents")
documents.add(File("resume.txt", 1024))
documents.add(File("report.pdf", 512000))
root.add(documents)

pictures = Folder("Pictures")
pictures.add(File("photo.jpg", 2048000))
root.add(pictures)

print("File system contents:")
root.list()  # Prints the hierarchy and calculates sizes recursively
