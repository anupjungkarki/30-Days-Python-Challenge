def factorial(num):
    if num == 1:
        return num
    else:
        return num * factorial(num - 1)


num = int(input("Enter Number To check Factorial:"))
if num < 0:
    print("Factorial Cannot Found for Negative Number.")
elif num == 0:
    print("Factorial of Zero(0) is 1")
else:
    print("Factorial is:", factorial(num))
