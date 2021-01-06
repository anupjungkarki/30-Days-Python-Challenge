# Lets see the method overloading and operator overloading in the python programming.

# What is method overloading ?
# Ans: Method overloading is the class having methods that are the same name with different arguments.

# Example
class OverLoadDemo:
    # first sum method with two argument
    def sum(self, a, b):
        s = a + b
        print(s)

    # overloaded sum method with three parameter
    def sum(self, a, b, c):
        s = a + b - c
        print(s)


object = OverLoadDemo()
object.sum(2, 4, 5)

# Look Operator Overloading also.
