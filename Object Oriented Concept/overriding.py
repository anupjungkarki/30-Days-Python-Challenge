# Overriding means having two methods with the same name but doing different tasks. It means that one of the methods override the other.
# In OOPS overriding concept which provide ability to change the implementation of a method in a child class which is already defined in one
# of its super class.

# Example
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def displayData(self):
        print('In parent class display data method')
        print('{} {}'.format(self.name, self.age))


class Employee(Person):
    def __init__(self, name, age, id):
        super().__init__(name, age)
        self.id = id

    def displayData(self):
        print('In child class display method')
        Person.displayData(self)  # calling
        print('{} {} {}'.format(self.name, self.age, self.id))


# Person class object
p1 = Person('Anup', 22)
p1.displayData()

# Employ class object
E1 = Employee('Ram', 50, 2345768)
E1.displayData()

# calling parent class overridden method from child class
E1 = Employee('Anup', 23, 3456677)
E1.displayData()
