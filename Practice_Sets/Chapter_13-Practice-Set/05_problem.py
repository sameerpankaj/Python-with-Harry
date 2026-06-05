#Write a program to find the maximum of the numbers is a list using the reduce function.

l = [1, 2, 333, 444, 555, 8888, 55, 33, 5555, 33, 44]

from functools import reduce

def greater(a, b):
    if (a>b):
        return a
    return b

print(reduce(greater, l))