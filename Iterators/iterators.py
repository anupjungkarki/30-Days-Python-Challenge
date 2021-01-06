# use of iterators in python
# Iterators in python are used within for loop, comprehension, generators e.t.c but they are hidden in plain sight
# Iterators in python is simply an object that can be iterated upon an object will return data, one element at a time.
# Python iterator object must implement two special methods. __iter__() and __next()__

# example
my_list = [4, 7, 0, 3]
my_iter = my_list.__iter__()
print(my_iter.__next__())
print(my_iter.__next__())
print(my_iter.__next__())
print(my_iter)


#  create an iterator
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x


obj = MyNumbers()
my_iter = iter(obj)
print(my_iter.__next__())


# Stop iteration example
print('Stop Iteration Example Below')
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration


data = MyNumbers()
my_iter = iter(data)

for x in my_iter:
    print(x)
