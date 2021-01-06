# Use of exception handling in the python programming
# In python exception handling is an abnormal situation during the execution.In general when an python program encounter a situation
# that it cannot cope with ,it raise an exception.So when an exception has occur then it must be handle the exception othewise  it
# terminate the exception.

# We have following keyword to handle exception in python
# try : the try block lets us to test a block of code for error.
# except : the except block lets us to handle the error.
# finally : the finally block lets us to execute code ,regardless of the result ofthe try and except block.
# We can also use else keyword in except block.


# simple example
try:
    x = 1 / 0

except:
    print('Something Went wrong!')


# example
def divide_num(num_list):
    for num in num_list:
        try:
            print(10 / num)
        except ZeroDivisionError as error:
            print(error)
            print('Zero is not valid argument here')
        else:
            print('In else block')


num_list = [5, 6, 0, 7]
divide_num(num_list)

# example with try,except,else and finally
try:
    num1, num2 = eval(input('Enter two number separated by commas:'))
    result = num1 / num2
    print('Result is:', result)
except ZeroDivisionError:
    print('division by zero error')
except SyntaxError:
    print('Comma is missing while given input enter like this example: 1 ,3')
else:
    print('No exception')
finally:
    print('This will execute no matter what')


# Raise exception
def enterAge(age):
    if age < 0:
        raise ValueError('Only positive integer are allowed')
    if age % 2 == 0:
        print('age is even')
    else:
        print('age is odd')


try:
    num = int(input('Enter your age:'))
    enterAge(num)
except ValueError:
    print('Only positive integer are allowed')
except:
    print('Something went wrong')
