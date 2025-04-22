class Animal:
    def __init__(self, name):
        self.name = name

    def move(self):
        print(f"{self.name} moves in a generic way.")

class Mammal(Animal):
    def move(self):
        print(f"{self.name} walks or runs.")

class Bird(Animal):
    def move(self):
        print(f"{self.name} flies 🐦.")

class Fish(Animal):
    def move(self):
        print(f"{self.name} swims 🐠.")

class Vehicle:
    def __init__(self, model):
        self.model = model

    def move(self):
        print(f"The {self.model} moves in a generic way.")

class Car(Vehicle):
    def move(self):
        print(f"The {self.model} is driving 🚗.")

class Plane(Vehicle):
    def move(self):
        print(f"The {self.model} is flying ✈️.")

class Boat(Vehicle):
    def move(self):
        print(f"The {self.model} is sailing ⛵.")

# Creating instances of different classes
my_dog = Mammal("Buddy")
my_sparrow = Bird("Chirp")
my_salmon = Fish("Finny")
my_sedan = Car("SedanX")
my_jet = Plane("SkyCruiser")
my_yacht = Boat("SeaDream")

# Calling the move() method on each object
animals_and_vehicles = [my_dog, my_sparrow, my_salmon, my_sedan, my_jet, my_yacht]

for item in animals_and_vehicles:
    item.move()