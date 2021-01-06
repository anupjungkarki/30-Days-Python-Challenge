# I/O operation are specially used to ask some user to give input in the python there are two inbuilt function to give input:

# input(prompt_message)
# raw_input(prompt_message): work in older version

x = int(input("Enter Your Mobile number:"))
print(x)

# taking multiple inputs from the user in python

# Using split() method
x, y = input("Enter the two values:").split()
print(x, y)

# Using List Comprehension
x, y = [int(x) for x in input("Enter two values:").split()]
print(x, y)

# use of end parameter : It gives space to two line string code
print("Hello,", end='')
print("world", end='')

# use of sep parameter: It will give ne line for two string
print("Hello,", sep='')
print("world", sep='')