# *args and **kwargs are the special symbol which are use to pass the arguments in python function
# *args is function definition in the python which is used to pass a variable number of arguments to a function
# When we prefix a function parameter with an asterisk(*) , it collects all unmatched positional arguments into tuples.

# **kwargs is  functional definition in the python which is used to pass a keyword , variable -length argument list.
# The ** double asterisk is used where it collect the new dictionary and where argument name are the keys and the corresponding
# dictionary values.

# Example
def use_of_args(*args):
    print(args)


use_of_args(1, 2, 3, 4)


def use_of_kwargs(**kwargs):
    print(kwargs)


use_of_kwargs(id=1, name='Anup', age=22)


# use of args and kwargs in same line to call function
def check_it(*args, **kwargs):
    print('args:', args)
    print('kwargs:', kwargs)


check_it(1, 2, 3, 4, id=1, name='Anup', age=22)
