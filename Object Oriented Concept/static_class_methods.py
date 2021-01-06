# Use of @staticmethod and @classmethod in python
# A @classmethod is a method that receives the class as the implicit first argument, just like an instance method receives the
# instance.This means we can use the class and its properties inside that method rather than a particular instance.
# @classmethod is basically a method of a class having access to every attribute of the class it was called on. Therefore a class method
# is a method that is bound to the class and not the object of the class.

# A @staticmethod is a method that knows nothing about the class or instance it was called on unless explicitly given.
# It just gets the arguments that were passed, no implicit first argument and It’s definition is immutable via inheritance.
# In simpler words a @staticmethod  is nothing more than a regular function defined inside a class that doesn’t have access
# to the instance therefore It is callable without instantiating the class.


# Class method ma chai directly class lai first argument linchha ani hamile yesma classmethod declare garera method ko through
# argument lai pass garna sakchhau ani class variable lai update grana pani sakchhau according to need without using instance method.

# Static method vaneko chai simple function jastai ho yesko relation na class ko instance sangha hunchha na method sangha simply
# hamilai class sangha related khi calculation cahiyo vane static method decleare gara kaam garna sakchhau.

# Example of classmethods aand staticmethod
from datetime import date
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def fromBirthYear(cls, name, year):
        return cls(name, date.today().year - year)

    @staticmethod
    def isAdult(age):
        if age > 18:
            return True
        return False


obj1 = Person('Anup', 22)
obj2 = Person.fromBirthYear('Anup', 1998)
print(obj1.age)
print(obj2.age)
print(Person.isAdult(23))


# Another Example
