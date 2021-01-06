# Nested Dictionary Values Access
data = {
    1: {
        "title": "Sample Konfabulator Widget",
        "name": "main_window",
        "width": 500,
        "height": 500
    },
    2: {
        "src": "Images/Sun.png",
        "name": "sun1",
        "hOffset": 250,
        "vOffset": 250,
        "alignment": "center"
    },
    3: {
        "data": "Click Here",
        "size": 36,
        "style": "bold",
        "name": "text1",
        "hOffset": 250,
        "vOffset": 100,
        "alignment": "center",
        "onMouseUp": "sun1.opacity = (sun1.opacity / 100) * 90;"
    }
}
print(data)
print(data[1])
# Access Items in a Nested Dictionary
print(data[3]['name'])

# Insert New Value To Neted Dictonary
data[3]['name'] = 'Anup Karki'
print(data)

# Delete Items From The Nested Dictonary
del data[2]
print(data)

# Iterate Through The Nested Dictionary
for key in data.keys():
    print(key)

for key, value in data.items():
    print("Id:", key)
    for k in value:
        data = value[k]
        print(k + '=', data)

# To Merge Nested Data
D1 = {'emp1': {'name': 'Bob', 'job': 'Mgr'},
      'emp2': {'name': 'Kim', 'job': 'Dev'}}

D2 = {'emp2': {'name': 'Sam', 'job': 'Dev'},
      'emp3': {'name': 'Max', 'job': 'Janitor'}}
D1.update(D2)
print(D1)
