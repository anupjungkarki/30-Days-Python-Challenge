# Simple Ca;culator Using Python Language
print('Select Number For Operation')
print("1.Add")
print("1.Substract")
print("1.Divide")
print("1.Multyply")
choice = input("Enter Choice 1/2/3/4:")
num1 = int(input("Enter The First Number:"))
num2 = int(input("Enter The Second Number:"))

if choice=='1':
    add=num1+num2
    print("The sum is:",add)
elif choice =='2':
    substract=num1-num2
    print("The Substract is:", substract)
elif choice == '3':
    divide=num1/num2
    print("The Divide is:", divide)
elif choice == '4':
    multiply=num1*num2
    print("The Multiply is:", multiply)
else:
    print("Invalid Input")

