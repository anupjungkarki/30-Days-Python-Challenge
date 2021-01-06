# The set operation of python are as follows

# union
a = {1, 2, 3, 4, 5}
b = {2, 4, 5, 8, 6}
union = (a | b)
print(union)
# or
union_sample = a.union(b)
print(union_sample)

# Intersection
sample_intersection = (a & b)
print(sample_intersection)
# or
sample_intersection = a.intersection(b)
print(sample_intersection)

# Difference
sample_difference = (a - b)
print(sample_difference)
# or
sample_difference = a.difference(b)
print(sample_difference)

# Symmetric difference
symmetric_difference = (a ^ b)
print(symmetric_difference)
# or
symmetric_difference = a.symmetric_difference(b)
print(symmetric_difference)

