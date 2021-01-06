# Here I am going to look about constructor and destructor in the python Object Oriented Programming.
# Constructor is used for initializing the instance members/variable when we create the object of a class.
# constructor are of two types default constructor and parameterized constructor.

# This is the example of default constructor where it doesn't accept any arguments.
class Demo:
    # constructor
    def __init__(self):
        # initializing instance variable
        self.num = 100

    # Method
    def read_number(self):
        print(self.num)


# creating a object of class.This invokes constructor
obj = Demo()
# calling the instance method using the object obj
obj.read_number()


# This is the example of the parameterized constructor where constructor with parameter is known as parameterized constructor.
class Addition:
    first = 0
    second = 0
    answer = 0

    # parameterized constructor
    def __init__(self, f, s):
        self.first = f
        self.second = s

    # Method
    def display(self):
        print("First Number:" + str(self.first))
        print("First Second:" + str(self.second))
        print("Answer:" + str(self.answer))

    # Method
    def calculation(self):
        self.answer = self.first + self.second


obj = Addition(100, 200)
obj.calculation()
obj.display()

# Destructor is not that much important in Python because python have garbage collector.
# If needed you can practice here
