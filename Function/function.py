# Use of function in python
# Function is the method of dividing the codes into useful blocks which can be reused.

# Simple function Calling
def hello():
    print('Hello,World')


hello()


#  Passing Arguments in Function
def sum(x, y):
    return x + y


result = sum(10, 5)
print(result)


# Default Arguments
def add(x=5, y=6):
    return x + y


print(add())


# Passing list as an arguments
def my_data(list_data):
    for x in list_data:
        print(x)


data = ['foo', 'bar', 'war']
my_data(data)


# return multiple values
def multiple_values(a, b):
    return a + b, a - b, a * b


result = multiple_values(3, 4)
print(result)


# Use of Nested function in python which is similar to closure
def nested1(a, b):
    def nested2(c, d):
        return c * d

    return nested2(a, b)


result = nested1(2, 5)
print(result)
