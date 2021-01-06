# Logical operators are used to join two or more conditions
# The logical operators are:

# and (Returns true if both statement are true)
x = 4
y = 9
if x > 0 and y < 9:
    print('fine')
else:
    print("error")

# or (Returns true if one of the  statement is true)
if x > 0 or y < 9:
    print('fine')
else:
    print('error')

# not (Reverse the result , return false if the result is true)
if not(x > 0 and y < 7):
    print('fine')
else:
    print('error')