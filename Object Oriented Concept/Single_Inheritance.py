# This is the example of single inheritance in python.
# In a single inheritance  derived class are inherit only from the parent class.
class Person:
    def __init__(self, name):
        self.name = name

    def get_details(self):
        return self.name


class Student(Person):
    def __init__(self, name, branch, year):
        super().__init__(name)
        self.branch = branch
        self.year = year

    def get_details(self):
        return "%s studies %s and is in %s year." % (self.name, self.branch, self.year)


class Teacher(Person):
    def __init__(self, name, paper):
        super().__init__(name)
        self.paper = paper

    def get_details(self):
        return "%s teaches %s" % (self.name, ",".join(self.paper))


obj = Person('Anup Karki')
print(obj.get_details())
obj = Student('Anup Karki', "BIT", '2017')
print(obj.get_details())
obj = Teacher('Anup Karki', ['Python'])
print(obj.get_details())
