matrix = [
    [1, 3, 5],
    [6, 7, 8],
    [0, 4, 2]
]
transpose = []
for i in range(3):
    transpose_row = []
    for row in matrix:
        transpose_row.append(row[i])
    transpose.append(transpose_row)
print(transpose)

# using list-comprehension in this nested list
transpose = [[row[i] for row in matrix] for i in range(3)]
print(transpose)

# Again we can also use
transpose = []
for i in range(3):
    transpose.append([row[i] for row in matrix])
print(transpose)
