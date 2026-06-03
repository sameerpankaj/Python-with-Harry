'''
The enumerate() function in Python lets you loop over an iterable and get both the index and the value at the same time.

Basic Syntax
enumerate(iterable, start=0)
iterable → list, tuple, string, etc.
start → optional starting index (default is 0)
Example 1: Without enumerate
fruits = ["apple", "banana", "orange"]

for i in range(len(fruits)):
    print(i, fruits[i])

Output:

0 apple
1 banana
2 orange
Example 2: With enumerate
fruits = ["apple", "banana", "orange"]

for index, fruit in enumerate(fruits):
    print(index, fruit)

Output:

0 apple
1 banana
2 orange

This is cleaner and more Pythonic.

Starting from a Different Number
fruits = ["apple", "banana", "orange"]

for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)

Output:

1 apple
2 banana
3 orange
Using with Strings
word = "Python"

for index, char in enumerate(word):
    print(index, char)

Output:

0 P
1 y
2 t
3 h
4 o
5 n
Converting to a List
fruits = ["apple", "banana", "orange"]

print(list(enumerate(fruits)))

Output:

[(0, 'apple'), (1, 'banana'), (2, 'orange')]

enumerate() returns an iterator of (index, value) tuples.

Common Interview Example

Find the position of an item:

fruits = ["apple", "banana", "orange"]

for index, fruit in enumerate(fruits):
    if fruit == "banana":
        print("Found at index", index)

Output:

Found at index 1
Why Use enumerate()?

Instead of:

for i in range(len(items)):
    print(i, items[i])

Prefer:

for i, item in enumerate(items):
    print(i, item)

It's:

More readable
Less error-prone
The preferred Python style
Summary
for index, value in enumerate(iterable):
    print(index, value)

enumerate() is the standard way to iterate over a sequence when you need both the index and the element.

'''
l = [3, 513, 53, 53, 535]


index = 0

# for item in l:
#     print(f'The item number {index} is {item} ')
#     index += 1

#This can be simplified using enumerate function

for index, item in enumerate(l):
    print(f'The item number at index {index} is {item}')
