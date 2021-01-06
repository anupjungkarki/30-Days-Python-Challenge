# Use of closure in the python
# To be a closure the function must be nested
def greet(message):
    def print_message():
        print(message)

    return print_message


another = greet("Hello, World")
another()

