# use of listInPython in the python
list_data_string = ['a', 'b', 'c', 'd', 'e']  # string listInPython
list_data_integer = [1, 2, 3]  # integer listInPython
list_data_mixed = [1, 'anup', 'katmmandu', 80]  # mixed listInPython
print(list_data_string)

# merging two listInPython data
list_concatenation = list_data_string + list_data_integer
print(list_concatenation)

# Accessing Elements of a listInPython
print(f"The Rollno is:", list_data_mixed[0])
print(f"The name is:", list_data_mixed[1])
print(f"The address is:", list_data_mixed[2])
print(f"The score is:", list_data_mixed[3])

# slicing in python
print(list_data_string[1:3])
print(list_data_string[-2:-1])

# changing the elements of listInPython
list_data_integer[1] = 5
print(list_data_integer)

# Append the listInPython items
list_append = ['foo', 'bar', 'sar', 'gar']
list_append.append('jar')
print(list_append)

list_append_empty = []
list_append_empty.append('foo')
print(list_append_empty)

# Insert an item as the particular  position
list_insert = ['foo', 'bar', 'sar', 'gar']
list_insert.insert(2, 'par')
print(list_insert)

# Extending the listInPython in python
first_list = ["name", 'address', 'phone']
second_list = ["country", "age", "occupation"]
first_list.extend(second_list)
print(first_list)

# deleting listInPython such as pop,remove,clear
first_list = ["name", 'address', 'phone']
second_list = ["country", "age", "occupation"]
first_list.remove('name')
second_list.pop(2)
del first_list[0]
print(first_list)
print(second_list)
# It will clear the whole listInPython data value and show empty listInPython
first_list.clear()
print(first_list)

# Zip in list
# If we wanted to create a list of lists that paired each name with a height,we could use the command zip.
# zip takes two (or more) lists as inputs and returns an object that contains a list of pairs.
# Example
names = ['Jenny', 'Alexus', 'Sam', 'Grace']
dogs_names = ['Elphonse', 'Dr. Doggy DDS', 'Carter', 'Ralph']
names_and_dogs_names = zip(names, dogs_names)
print(names_and_dogs_names)
list_of_names_and_dogs_names = list(names_and_dogs_names)
print(list_of_names_and_dogs_names)
