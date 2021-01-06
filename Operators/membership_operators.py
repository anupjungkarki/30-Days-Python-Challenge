# Membership operators are used to check is a specific item is present in a sequence(such as string, tuples , list or range ) or
# collection a collection such as a dictionary , set or frozen set.
# The membership operators are:

# in (Returns True if a value is present in the sequence)
list_data = ['foo', 'bar', 'car']
if 'foo' in list_data:
    print(list_data[0])
else:
    print('Not Found')

# not in (Returns True if a value is not present in the sequence)
if 'foo' not in list_data:
    print('Not found')
else:
    print(list_data[0])
