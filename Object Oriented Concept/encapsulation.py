# Encapsulation is one of the method of the fundamental concept in object oriented programming(OOP).Other programming have access specifier
# to handle with the private data but in python private data is easily access from the outside of the class so Encapsulation helps to
# restrict to access data and variable outside the class.

# Here access of private key is possible
class Car:
    def __init__(self, name, mileage):
        self._name = name
        self.mileage = mileage

    def description(self):
        return f'The{self._name} car gives the mileage of {self.mileage} km/1hr'


obj = Car('BMW 7-Series', 39.53)
# accessing the protected variable by class method
print(obj.description())

# accessing the protected variable directly from outside
print(obj._name)
print(obj.mileage)


# Now lets work some encapsulation method
class Car:
    def __init__(self, name, mileage):
        self.__name = name  # Private Variable
        self.mileage = mileage

    def description(self):
        return f'The {self.__name} car given the mileage of {self.mileage} km/1hr'


obj = Car('BMW 7-Series', 39.53)
# Accessing the private variable by class method
print(obj.description())
# Accessing the private variable directly from the outside
# print(obj.__name)
# print(obj.mileage)

# It give an error while trying to access from the outside the class but we can also access by using Name MANGLING
# print(obj.mileage)
# print(obj._car__name)  # mangled name

