# use of while loop in python
num = 20
while True:
    data = int(input("Enter The Number:"))
    if data > num:
        print("The Input Data is greater than 20 Try Again")
        continue
    else:
        print(data)
        break


a = 0
while a <= 5:
    a = a+1
    print("While Loop")


input1 = int(input("Enter the number1:"))
input2 = 0
while input2 <= 9:
    input2 = input2 + 1
    cal = input1 * input2
    print(input1, "*", input2, "=", cal)
