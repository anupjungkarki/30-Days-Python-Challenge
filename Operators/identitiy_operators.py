# Identity operators are used to check if the two objets point to the same object, with the same memory location.
# the identity operators are:

# is (Returns true if both variables are the same object)
list_one = ['foo', 'zoo', 'boy']
list_two = ['foo', 'zoo', 'boy']
if list_one is list_two:
    print(True)
else:
    print(False)

# is not ( Returns true if both variables are not the same object)
if list_one is not list_two:
    print(True)
else:
    print(False)