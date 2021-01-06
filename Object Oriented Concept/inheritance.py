# Here is the concept of inheritance in the python programming.
# Inheritance allows us to define a class that inherit all the method and properties from another class
# Parent class is the class being inherit from ,also called base class.
# Child class is that class that inherit from another class , also called derived class.

# Python Inheritance Syntax
class BaseClass:
    pass


# body of the base class
class DerivedClass:
    pass


# Body of the Derived Class
# Derived class inherit features from the base class where new features can be added to it.This result is re-usable code.

# Simple Example of Inheritance
class Person:
    def __init__(self, name, id_number):
        self.name = name
        self.id_number = id_number

    def display_data(self):
        print(self.name + " id is " + str(self.id_number) + " his salary is " + str(
            self.salary) + " he is an aspiring " + self.post)


# child class
class Employee(Person):
    def __init__(self, name, id_number, salary, post):
        self.salary = salary
        self.post = post
        # invoking the  __init__ of the parent class
        Person.__init__(self, name, id_number)


obj = Employee('Anup', 32435, 200000, 'Data Scientist')
obj.display_data()


# Another example
class Vehicle:
    def __init__(self, name, color):
        self.__name = name
        self.__color = color

    def getColor(self):
        return self.__color

    def getName(self):
        return self.__name


class Car(Vehicle):
    def __init__(self, name, color, model):
        super().__init__(name, color)
        self.__model = model

    def getDescription(self):
        return self.getName() + self.__model + "in" + self.getColor() + "color"


obj = Car("Mustang Ford", "Black", "GT3450")
print(obj.getDescription)
print(obj.getName())



