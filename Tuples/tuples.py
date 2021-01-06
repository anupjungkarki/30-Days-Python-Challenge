# use of tuples in python
# Tuples is a collection of Python object much like a list but it is immutable

# Simple tuples
test_tuples = (1, 3, 4)
print(type(test_tuples))
print(test_tuples)

# use of mixing tuples
tuple2 = (1, 2, 'anup', 'karki')
print(tuple2)

# Accessing the items in the tuples
tuple_access = (1, 2, 3, 'foo', 'bar')
access = tuple_access[3]
print(access)

#  concatenation of tuples
tuple1 = (1, 2, 3)
tuple2 = ('anup', 'karki')
con_tup = (tuple1 + tuple2)
print(con_tup)

#  Nested operation on the tuples
tuple1 = (1, 2, 3)
tuple2 = ('anup', 'karki')
con_tup = (tuple1, tuple2)
print(con_tup)

# Slicing operation on the tuples
slice_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
sliced = slice_tuple[3:6]
print(sliced)
sliced = slice_tuple[-6:-3]
print(sliced)

# Find the length of the tuples
print(len(slice_tuple))

# Changing the tuples only possible in nested tuples where list is there
slice_tuple = (1, 2, 3, 4, 5, [6, 7, 8, 9, 10])
slice_tuple[5][4] = 20
print(slice_tuple)

# Inbuilt function in the tuples
# max
check_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(max(check_tuple))

# min
print(min(check_tuple))

# sum
print(sum(check_tuple))

# sorted
print(sorted(check_tuple))

# use tuples as keys in the dictionary
tuple_key = {('blue', 'sky'): 'Good', ('red', 'blood'): 'Bad'}
print(tuple_key)

# Packing and unpacking
person_status = ('Anup', '5ft', 'Programmer')
(name, height, profession) = person_status
print(name, height, profession)

# Iterate through the tuples
person_status = ('Anup', '5ft', 'Programmer')
for data in person_status:
    print(data)

# If else
if 'Anup' in person_status:
    print('Yes')
else:
    print('NO')
