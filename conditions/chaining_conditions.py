# Use Of Chaining Condition in Python
a = 10
b = 30
c = 120
if a > b > c:
    print("a value is greater than other values")
elif b > a and b > c:
    print("b value is greater than other values")
else:
    print("c value is greater than other values")
