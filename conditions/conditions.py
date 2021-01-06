# There are three types condition statement in python that are if, elif and else
name = input("Enter The Name:")
x = int(input("Enter The First Value:"))
y = int(input("Enter The Second Value:"))
z = int(input("Enter Teh Third Value:"))
add = ''
if name == "anup":
    add = x + y + z
    print(add)
elif name == "karki":
    print("Karki is found")
else:
    print("Nothing")

# Practice of Nested If Else In Python
a = int(input("Enter The Number:"))
if a >= 0:
    if a == 0:
        print("Zero")
    else:
        print("Non Zero Value Found")
else:
    print("Negative Value Is Found")


