def test() :
    yield 1
    yield 2
    yield 3

gen = test()

print(next(gen))
print(next(gen))
print(next(gen))