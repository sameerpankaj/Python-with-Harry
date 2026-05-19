s = {1, 2, 3, 4, 5, 'Harry'}

e = set()# Empty set

print(s)# Output: {1, 2, 3, 4, 5}
print(type(s))# Output: <class 'set'>

s.add(6)
print(s)  # Output: {1, 2, 3, 4, 5, 'Harry', 6}

print(s, type(s))  # Output: {1, 2, 3, 4, 5, 'Harry', 6} <class 'set'>

#sets are unordered, mutable, and do not allow duplicate elements. They are defined using curly braces {} or the set() constructor. Sets are commonly used for membership testing, removing duplicates from a sequence, and performing mathematical operations like union, intersection, and difference.    
#sets are useful for storing unique elements and performing operations like union, intersection, and difference. They are commonly used in various applications, such as removing duplicates from a list, checking for membership, and performing set operations in mathematics. In summary, sets are a powerful data structure in Python that allow us to store and manipulate unique elements efficiently.
#In summary, sets are a powerful data structure in Python that allow us to store and manipulate unique elements efficiently.