students = {
    'Name': 'Anup',
    'Address': 'Kathmandu',
    'Section': 'A',
    'Semester': 6,
    'Year': 3,
    'Rollno': 1,
}
print(students)

for key, value in students.items():
    print(key, "=", value)

# Other Method to Get Data
for key in students.keys():
    values = students[key]
    print(key, '=', values)
