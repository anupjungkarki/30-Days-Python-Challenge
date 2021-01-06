# use of generator in the python
# Generators are iterators , but we can only iterate once because they do not store all the values in memory ,they generate the value on the fly.

# Example of generator
def generator_function():
    for i in range(10):
        yield i


for items in generator_function():
    print(items)


# Generator square number
def square_number(nums):
    for i in nums:
        yield i * i


data = square_number([1, 2, 3, 4, 5, 6, 7])
print(data)
print(next(data))
print(next(data))
print(next(data))

# Comprehension use in generator
my_nums = (i * i for i in [1, 2, 3, 4, 5, 6, 7])
print(my_nums)
print(list(my_nums))

# Other example
odd_numbers = (num for num in range(5) if num % 2 != 0)
print(odd_numbers)
print(list(odd_numbers))

