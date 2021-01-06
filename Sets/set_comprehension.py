# use of set comprehension in python programming
# using loop method
set1 = {0, 1, 2, 3, 4, 5, 6}
print(set1)
new_set1 = set()
for i in set1:
    new_set1.add(i + 1)
print('Output using loop:', new_set1)

# same example using set comprehension
set2 = {0, 1, 2, 3, 4, 5, 6}
new_set2 = {i + 1 for i in set1}
print('Output using List Comprehension:', new_set2)

# use range in set comprehension
new_set = set()
for i in range(20):
    new_set.add(i + 1)
print(new_set)

# same example using set comprehension
new_set3 = {i + 1 for i in range(20)}
print(new_set3)

# print value divided  by 2
set4 = set()
for i in range(20):
    if i % 2 == 0:
        set4.add(i)
print(set4)

# using set comprehension same problem
set5 = set()
new_set5 = {i for i in range(20) if i % 2 == 0}
print(new_set5)

# nested loop
set4 = set()
for i in range(20):
    if i % 2 == 0:
        if i % 3 == 0:
            set4.add(i)
print(set4)

# set comprehension nested loop
new_set5 = {i for i in range(20) if i % 2 == 0 if i % 3 == 0}
print(new_set5)

# if else in loop
set_data = set()
for i in range(10):
    if i % 2 == 0:
        set_data.add(i)
    else:
        set_data.add(i * 100)
print(set_data)

# set comprehension  using if else
set_data = {i if i % 2 == 0 else i * 100 for i in range(10)}
print(set_data)
