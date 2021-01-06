#  Use of property decorator and getter and setter in python
# The @property decorator is the built in decorator in the python programming which is helpful change the class methods or attributes
# in such a way that the user of class no need to make change in their code.The main objective of the any decorator is to modify
# class methods or attributes in such a way that the user of class no need to make change in their code. Property decorator is use
# to achieve the getter and setter method

# What is getter and setter?
# Getter: These are the methods used in OOPS which helps to access the private attributes from the class.

# Setter : These are the methods used in OOPS feature which help to set the value to private attributes class.

# Example
class Student:
    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.fullname = self.first + ' ' + self.last

    # generate email using first and last
    def getEmail(self):
        return '{}.{}@info.com.np'.format(self.first, self.last)


# student1
student1 = Student('anup', 'karki')
print(student1.fullname)
print(student1.getEmail())

# updating the student1 object first name
student1.first = 'john'
print(student1.fullname)
print(student1.getEmail())


# In the above example the email  changed with first name change because it is simple variable but fullname is not changed with
# where fullname is derived from the above variable so to overcome this problem we use property decorator and setter , getter methods.
class Student:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def fullname(self):
        return self.first + ' ' + self.last

    def getEmail(self):
        return '{}.{}@info.com.np'.format(self.first, self.last)


# student1
student1 = Student('anup', 'karki')
print(student1.fullname)
print(student1.getEmail())

# updating the student1 object first name
student1.first = 'john'
print(student1.fullname)
print(student1.getEmail())


# In the above example property decorator is used on function name and function will worked as a fullname attributes and also can work as
# getter because of the property decorator attached to it.

# Now lets implement the deleter and setter methods
# Deleter methods will delete the attributes from memory

class Student:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def fullname(self):
        return self.first + ' ' + self.last

    # Setter for the fullname
    @fullname.setter
    def fullname(self, name):
        # Split the name from space
        first, last = name.split(' ')
        self.first = first
        self.last = last

    # Deleter for the fullname
    @fullname.deleter
    def fullname(self):
        self.first = None
        self.last = None
        print('Deleted the fullname')

    # generate email using first and last name
    def getEmail(self):
        return '{}.{}@info.com.np'.format(self.first, self.last)


# student1
student1 = Student('anup', 'karki')
print(student1.fullname)
print(student1.getEmail())

# updating the student1 object first name
student1.first = 'john'
print(student1.fullname)
print(student1.getEmail())

# setting new value of fullname
student1.fullname = 'karki vai'
print(student1.fullname)
print(student1.getEmail())

# deleting the fullname
del student1.fullname
