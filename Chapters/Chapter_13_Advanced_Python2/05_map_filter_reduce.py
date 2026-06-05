from functools import reduce

#map
_lsit = [1, 2, 3, 4, 5]

square = lambda x:x*x

sqList = map(square, _lsit)
print(list(sqList))

#filter
def even(n):
    if (n%2 == 0):
        return True
    return False


onlyEven = filter(even, _lsit)
print(list(onlyEven))

#reduce
def sum(a, b):
    return a + b

print(reduce(sum, _lsit))