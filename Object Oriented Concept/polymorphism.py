# Use of Polymorphism in the python programming.
# The word polymorphism means having many forms.In programming polymorphism means same function name but different signature. So we can
# use same function name for different types.

# Example of polymorphism
class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth


class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2


rec = Rectangle(10, 20)
squ = Square(10)
print(f'The area of Rectangle is:', rec.area())
print(f'The area of Square is:', squ.area())


# Another example  of polymorphism with inheritance
class Animal:
    def type(self):
        print("Various types of animals")

    def age(self):
        print("Age of the animals")


class Rabbit(Animal):
    def age(self):
        print("Age of the Rabbit")


class Horse(Animal):
    def age(self):
        print("Age of the Horse")


obj_animal = Animal()
obj_rabbit = Rabbit()
obj_horse = Horse()

obj_animal.type()
obj_animal.age()

obj_horse.type()
obj_horse.age()

obj_rabbit.type()
obj_rabbit.age()
