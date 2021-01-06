# This the use of OOP Concept in Python Programming with Core concept
# Python Object Oriented Approach

# Class
# A class is a blueprint from which individual objects are created.

# Object
# An object is a instance of a class.

# Self Parameter: self parameter refers to the individual object itself, It is used to fetch or set attributes of the particular instance.
# We can call any things here but self is a standard method here in python.

# Attributes : Attributes are the individual things that differentiate one object from another.They determine the appearance ,state ,or
# other qualities of that object.For example Car is a class it might have following attributes such as style,color,wheel,size,seated

# __init__() Method : __init__() is the special method that initializes an individual object.
# This method runs automatically each time an object of class is created.

# Instance Attributes: The instance attributes is a variable that is unique to each object(instance).Every object of that class has is own
# own copy of that variable.Any change made to the variable don't reflect in other object of class.

# Class Attributes : The class attributes is a variable that is same for all objects.And there is only one copy of that variable that is
# shared with all objects.Any change made to that variable will reflect in all other object.

# Object : An object(instance) is an instantiation of a class.It is a entity that has attributes and behaviour.For example Ram is a object
# who has attributes such as height ,weight , color etc. and certain behaviour such as walking , eating , talking , sleeping etc.

class Car:
    # Class attributes
    wheels = 4

    # initializer
    def __init__(self, color, style):  # instance attributes
        self.color = color
        self.style = style


obj = Car('Black', 'Sedan')
# Access attributes
print(obj.style)
print(obj.color)
# Modify attributes
obj.style = "Shiny"
print(obj.style)


# Methods : Methods determine what types of functionality a class has, how it handles its data, and its overall behaviour.

# Instance Methods: Instance Method are nothing but functions defined inside a class that operates on instance of that class.
class Car:
    def __init__(self, color, style):
        self.color = color
        self.style = style

    # Let give method one
    def showDescription(self):
        print("The car is a", self.color, "and It's Style is", self.style)

    # Lets make method two
    def changeColor(self, color):
        self.color = color


obj = Car("Black", "Sedan")
obj.showDescription()

obj.changeColor("White")
obj.showDescription()
del obj.style  # It delete the attributes property
del obj  # It will delete the object property


# Hiding data fields: To hide data fields we need to define private data field.In Python we can create private data field
# using two leading underscore.We can also define a private method using two leading underscores.
class BankAccount:
    # constructor of initializer
    def __init__(self, name, money):
        self.__name = name
        self.__balance = money  # __ balance is private now , so it only accessible inside the class.

    def deposit(self, money):
        self.__balance += money

    def withdraw(self, money):
        if self.__balance > money:
            self.__balance -= money
            return money
        else:
            return "Insufficient Funds"

    def CheckBalance(self):
        return self.__balance


obj = BankAccount('Anup', 200)
print(obj.withdraw(400))
obj.deposit(200)
print(obj.CheckBalance())
print(obj.withdraw(200))
print(obj.CheckBalance())


# Practice from Corey  and Understanding Instance Variables and Class Variables
# Instance Variable are those variable where they are unique for each instance objects change in any things only affect its
# particular called instance object  where Class variable are those variable They are same for all instance of the class we can also change the
# class variable for particular object using instance variable reference which is shown below.
class Employee:
    num_of_emp = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emp += 1

    def fullName(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * raise_amt)


emp_1 = Employee('anup', 'karki', 30000)
emp_2 = Employee('ram', 'karki', 40000)
emp_1.raise_amt = 1.07
print(emp_1.raise_amt)
print(emp_2.raise_amt)
print(Employee.raise_amt)
# print(emp_1.first)
# print(Employee.num_of_emp)
