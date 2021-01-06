# ways of creating simple string
string1 = 'Hello! World1'
string2 = "Hello! World2"
print(string1)
print(string2)

# multi-line string
string = '''Hello python programmers'''
print(string)
string_2 = """Hello Nepali Programmers"""
print(string_2)

# Accessing the string in python
string_access = "Hello Programmers"
access = string_access[2]
print(access)
print(string_access[-2])

# Use of loop in strings
for data in string_access:
    print(data)

if "e" in string_access:
    print("Data is found!")
else:
    print("Data not found!")

# Upper and Lower string
string_to_upper = "Hello"
data = string_to_upper.upper()
print(data)

# Concatenation of strings in Python
print(string1 + string_2)

# Repeating of string
repeating = "no sense"
data = repeating * 4
print(data)

# The replace() method replaces a string with another string
r = "Hello, Anup"
print(r.replace("Hello!", "World"))

# Escape Sequence in Python String
xyx = "To access substrings, use the square brackets \n for slicing along with the index or indices to obtain your substring."
print(xyx)

pq = "I'm \"Anup\""
print(pq)

fg = "Hello \ nepali "
print(fg)

# String Formatting
string_format = "{} {} {} {} ".format('My', 'Name', 'is', 'Anup')
print(string_format)

# Positional Formatting
string_format_next = "{2} {0} {1} {3}".format('Name', 'is', 'My', 'Anup')
print(string_format_next)

# keyword formatting
keyword_string = "{a} {k}".format(a='Anup', k='karki')
print(keyword_string)

# f-String Formatter
name = 'Bob'
age = 25
S = f"{name} is {age} years old."
print(S)
