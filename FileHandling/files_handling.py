# Use of files handling in the python programming.
# Reading the file
f = open("hello.txt", "r")
print(f.read())
f.close()

# Read only part of file
f = open("hello.txt", 'r')
print(f.read(5))
f.close()

# read line and lines of the file
f = open("hello.txt", "r")
print(f.readline())
print(f.readlines())
f.close()

# looping
f = open("hello.txt", "r")
for data in f:
    print(data)


# Writing in the file in append mode
f = open('hello.txt', 'a')
f.write("\n Now writing in the files")
f.close()

# writing  file in write mode
f = open('hello.txt', 'w')
f.write('This will delete the file content and rewrite it.')
f.close()

