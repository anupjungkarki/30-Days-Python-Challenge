# use for for loop in python
data = {'cat', 'mat', 'rat', 'bat', 'hat'}
for items in data:
    print(items)

student_name = 'anup'
marks = {'Python': 78, 'Java': 89, 'C++': 97}
for student in marks:
    if student == student_name:
        print(marks[student])
else:
    print("Student Not Found in Search")

mul = 65
print("====The Multiplication table is====")
for x in range(11):
    print(mul * x)
