a = (1, 45, 342, 3424, False, "Rohan", 45, 'Shivam') # Creating a tuple with different data types.
print(a) # Output: (1, 45, 342, 3424, False, 'Rohan', 45, 'Shivam')

no = a.count(45) # This will count the number of occurrences of the value 45 in the tuple a.
print(no) # Output: 2, because the value 45 appears twice in the tuple a.

i = a.index(45) # This will return the index of the first occurrence of the value 45 in the tuple a.
print(i) # Output: 1, because the value 45 is located at index 1 in the tuple a. Note that if the value 45 were not present in the tuple, this line would raise a ValueError.


print(len(a)) # Output: 8, because the tuple a contains 8 elements.
print(i) # Output: 1, because the element at index 0 in the tuple a is 1.