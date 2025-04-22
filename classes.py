# Base class: Person
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Subclass: Superhero (inherits from Person)
class Superhero(Person):
    def __init__(self, name, age, alias, power, city):
        super().__init__(name, age)
        self.alias = alias
        self.power = power
        self.city = city
        self.is_in_disguise = True

    def reveal_identity(self):
        self.is_in_disguise = False
        return f"{self.alias} is actually {self.name}!"

    def use_power(self):
        return f"{self.alias} uses {self.power}! 💥"

    def patrol_city(self):
        return f"{self.alias} is watching over {self.city} 🏙️"

# Example object
hero1 = Superhero("Diana Prince", 900, "Wonder Woman", "Super Strength", "Themyscira")
print(hero1.patrol_city())
print(hero1.use_power())
print(hero1.reveal_identity())

# Base class
class Vehicle:
    def move(self):
        return "The vehicle moves."

# Subclasses with polymorphic behavior
class Car(Vehicle):
    def move(self):
        return "Driving on the road 🚗"

class Plane(Vehicle):
    def move(self):
        return "Flying through the sky ✈️"

class Boat(Vehicle):
    def move(self):
        return "Sailing across the sea 🚢"

class Bicycle(Vehicle):
    def move(self):
        return "Pedaling down the lane 🚴"

# Function that accepts any Vehicle and calls move()
def travel(vehicle):
    print(vehicle.move())

# Test polymorphism
travel(Car())
travel(Plane())
travel(Boat())
travel(Bicycle())
