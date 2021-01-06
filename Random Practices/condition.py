print("Enter The Marks Here:")
number= int(input())
print(number)

if number>90 and number<100:
    grade= 'A'

elif(number>80 and number<90):
    grade= 'B+'

elif(number>70 and number<80):
    grade= 'B'
else:
   grade='Nothing found'
   
print("The Grade is:",grade)
