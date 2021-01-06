# Simple Steps To store Data In the Dictionary
mydic = {'Name': 'Anup',
         'Country': 'Nepal',
         'Address': 'Solukhumbu',
         'Age': 22}
print(mydic)

# Other Way Of storing Dictonary

dic = dict(Name="Anup", Address="Solukhumbu", Age=22)
print(dic)

# To access The Value From The Above Dictonary
# Keys is Name
name = mydic['Name']
country = mydic['Country']
print(name, country)

# To add New Values To the Particular Dictonary

mydic["email"] = "anupkarki@gmail.com"
print(mydic)

# To delete Values From The Dictonary

del mydic['Age']
print(mydic)

# If Condition in the Dictonary
mydict = {'Name': 'Anup',
          'Country': 'Nepal',
          'Address': 'Solukhumbu',
          'Age': 22}

if 'Name' in mydict:
    value = mydict['Name']
    print(value)
    # print(mydict['Name'])

# Use of Exception In Dictonary
try:
    print(mydict['Address'])
except:
    print('Woops!! Error In Fetching Data From Dictonary.')

# Looping Through The Dictonary

# To get Keys 
for key in mydict.keys():
    print(key)

# To get Values
for values in mydict.values():
    print(values)

# To getting Both Keys and Values
for key, value in mydict.items():
    print(key, value)

# Copy the Dictionary Key and Values
mydic_copy = mydict.copy()  # or
# mydic_copy = dict(mydic) To copy We can Also Asssign Like This
print(mydic_copy)

mydic_copy['Toll'] = 'Simkharka'
print(mydic_copy)

# Merge the To dictionary
data = {'FirstName': 'Anup', 'MiddleName': 'Jung', 'LastName': 'Karki'}
info = {'Email': 'anupkarki2012@karki.com', 'Address': 'Kathmandu,Nepal', 'Contact': '9803456234'}
data.update(info)
print(data)

# Number In Dictionary

data = {1: 8, 2: 9, 3: 10}
values = data[1]
print(values)
