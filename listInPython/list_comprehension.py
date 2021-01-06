# use in normal loop form
square = []
for i in range(10):
    square.append(i * i)
print(square)

# List comprehension is the process of creating/making new list from the existing list
# list comprehension
list_com = [i ** 2 for i in range(0, 10)]
print(list_com)

# use in complex form
list_a = [1, 3, 6, 9, 12, 15]
list_b = []
for number in list_a:
    if number % 4 == 0:
        list_b.append(number)
print(list_b)

# same with list comprehension
list_a = [1, 3, 6, 9, 12, 15]
list_b = [number for number in list_a if number % 4 == 0]
print(list_b)

# Another realtime example
students = [
    {
        "name": "Jacob Martin",
        "father name": "Ros Martin",
        "Address": "123 Hill Street",
    }, {
        "name": "Angela Stevens",
        "father name": "Robert Stevens",
        "Address": "3 Upper Street London",
    }, {
        "name": "Ricky Smart",
        "father name": "William Smart",
        "Address": "Unknown",
    }
]
# using loop to find the list particular data
name_list = []
for student in students:
    name_list.append(student["name"])
print(name_list)

# using list comprehension
# syntax for list comprehension = [expression for item in list if conditional]
name_list = [student["name"] for student in students]
print(name_list)


