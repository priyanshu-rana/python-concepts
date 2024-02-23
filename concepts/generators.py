# generator function
def simpleGeneratorFunc():
    yield 1
    yield 2
    yield 3


# x is a generator object
x = simpleGeneratorFunc()

print(next(x))
print(next(x))
print(next(x))
