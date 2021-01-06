from functools import reduce
# Map , Filter , Reduce are paradigms of  functional programming. They allow to write simpler , shorter code.

# Map
# The syntax of map  function in the python -> map(function,*iterables)

# example
square = lambda x: x ** 2
result = map(square, [1, 2, 3, 4, 5, 6, 7, 8])
print(list(result))

# Filter
# The syntax of filter  function in the python -> filter(function,*iterables)

# example
even = lambda x: x % 2 == 0
result = filter(even, [1, 2, 3, 4, 6, 7, 8, 9])
print(list(result))

# reduce
mul = lambda x, y: x * y
result = reduce(mul, range(2, 8))
print(result)



