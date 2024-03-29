class Bird:
    def fly(self):
        print("Flying...")

    def make_sound(self):
        pass


class Ostrich(Bird):
    def fly(self):
        # Ostriches can't fly, so we override the fly method
        print("Sorry, I can't fly.")


# Function to perform actions for a list of birds
def perform_actions(birds):
    for bird in birds:
        bird.fly()
        bird.make_sound()


# Usage
bird = Bird()
ostrich = Ostrich()

birds = [bird, ostrich]
perform_actions(birds)


class Bird:
    def make_sound(self):
        pass


class Ostrich(Bird):
    def make_sound(self):
        print("Brrr...")


# Function to perform actions for a list of birds
def perform_actions(birds):
    for bird in birds:
        bird.make_sound()


# Usage
bird = Bird()
ostrich = Ostrich()

birds = [bird, ostrich]
perform_actions(birds)
