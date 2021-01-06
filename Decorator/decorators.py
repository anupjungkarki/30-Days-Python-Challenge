# Use of decorators in the python
# A decorator takes in a function ,adds some functionality and returns it.
# It is an interesting features of python to add functionality to an existing code.

# Basic steps before  going through the decorator
def is_called():
    def is_return():
        print("Hello, Friends")

    return is_return


new_funk = is_called()
new_funk()


# Use of decorator
def make_decorator(func):
    def inner():
        print("I got decorator ")
        func()

    return inner


def ordinary():
    print("I am ordinary")


ordinary()
# lets decorate this ordinary function which we are currently working
assign_decorator = make_decorator(ordinary)
assign_decorator()

print(
    "=================The below example is equivalent to above example using @ symbol for decorator======================")


# We can use @ symbol for decorating the function the example is given below
@make_decorator
def ordinary():
    print("I am ordinary assign using @ decorator")


ordinary()


# The above decorator was simple and it only worked with function that did not have any parameters
# This is a example what if we have parameters
def smart_division(func):
    def inner(a, b):
        print("I am going to divide ", a, "and ", b)
        if b == 0:
            print("Whoops! Cannot divide")
            return
        return func(a, b)

    return inner


@smart_division
def divide(a, b):
    print(a / b)


divide(2, 5)


# Chaining decorator in the python
def star(func):
    def inner(*args, **kwargs):
        print("*" * 30)
        func(*args, **kwargs)
        print("*" * 30)

    return inner


def percentage(func):
    def inner(*args, **kwargs):
        print("%" * 30)
        func(*args, **kwargs)
        print("%" * 30)

    return inner


@star
@percentage
def printer(msg):
    print(msg)


printer("Hello")

