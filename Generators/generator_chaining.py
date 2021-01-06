# chaining in generators
def integers():
    for i in range(1, 5):
        yield i


def squared(seq):
    for i in seq:
        yield i * i


def negated(seq):
    for i in seq:
        yield -i


initial = integers()
print(list(initial))

# passing the initial value to squared
sq_chain = squared(integers())
print(list(sq_chain))

# passing sq_chain to negated generator
negated_data = negated(squared(integers()))
print(list(negated_data))
