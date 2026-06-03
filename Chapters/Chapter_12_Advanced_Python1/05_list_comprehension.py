'''
List comprehension is a concise way to create lists in Python using a single line of code.

Basic Syntax
new_list = [expression for item in iterable]
Example
squares = [x ** 2 for x in range(5)]
print(squares)

Output:

[0, 1, 4, 9, 16]
Equivalent for Loop
squares = []

for x in range(5):
    squares.append(x ** 2)

print(squares)

List comprehensions are shorter and often easier to read.

Using Conditions
Even Numbers
evens = [x for x in range(10) if x % 2 == 0]
print(evens)

Output:

[0, 2, 4, 6, 8]
Transforming Strings
words = ["python", "java", "c++"]

upper_words = [word.upper() for word in words]

print(upper_words)

Output:

['PYTHON', 'JAVA', 'C++']
Conditional Expression
numbers = [1, 2, 3, 4, 5]

labels = ["Even" if n % 2 == 0 else "Odd" for n in numbers]

print(labels)

Output:

['Odd', 'Even', 'Odd', 'Even', 'Odd']
Nested List Comprehension
matrix = [
    [1, 2],
    [3, 4],
    [5, 6]
]

flat = [num for row in matrix for num in row]

print(flat)

Output:

[1, 2, 3, 4, 5, 6]
Creating a List of Tuples
pairs = [(x, y) for x in range(3) for y in range(2)]

print(pairs)

Output:

[(0, 0), (0, 1), (1, 0), (1, 1), (2, 0), (2, 1)]
Common Interview Examples
Get Length of Each Word
words = ["apple", "banana", "orange"]

lengths = [len(word) for word in words]

print(lengths)

Output:

[5, 6, 6]
Remove Spaces
text = "Hello World"

chars = [c for c in text if c != " "]

print(chars)

Output:

['H', 'e', 'l', 'l', 'o', 'W', 'o', 'r', 'l', 'd']
When Not to Use List Comprehensions

Avoid overly complex comprehensions:

# Hard to read
result = [x*y for x in a if x > 0 for y in b if y < 0]

In such cases, a regular for loop may be clearer.

Summary
# Basic
[expression for item in iterable]

# With condition
[expression for item in iterable if condition]

# If-else expression
[expr1 if condition else expr2 for item in iterable]

List comprehensions are one of the most commonly used Python features for creating and transforming lists efficiently and readably.

'''
myList = [1, 2, 9, 5, 3, 5]

# squaredList = []
# for item in myList:
#     squaredList.append(item*item)
    
squaredList = [i*i for i in myList]
print(squaredList)
