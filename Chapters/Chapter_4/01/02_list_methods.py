
friends = ["Apple", "Ornange", 5, 345.06, False,  "Charlie", "David"]

print(friends) # Output: ['Apple', 'Ornange', 5, 345.06, False, 'Charlie', 'David']
# Lists have various built-in methods that allow you to perform operations on them. Here are some commonly used list methods:   


# 1. append(): Adds an element to the end of the list.      
friends.append("Harry") # Adding "Harry " to the end of the list.

print(friends) # 

#sort method is used to sort the elements of a list in ascending order. It modifies the original list and does not return a new list. The sort() method can be used with various data types, including numbers and strings. When sorting strings, it sorts them in alphabetical order. When sorting numbers, it sorts them in numerical order.
numbers = [5, 2, 9, 1, 3]
numbers.sort()
print(numbers) # Output: [1, 2, 3, 5, 9]   

numbers.sort(reverse=True) # Sorting in descending order
print(numbers) # Output: [9, 5, 3, 2,

numbers.insert(2, 10) # Inserts the value 10 at index 2
print(numbers) # Output: [9, 5, 10, 3, 2, 1]

numbers.remove(3) # Removes the first occurrence of the value 3 from the list
print(numbers) # Output: [9, 5, 10, 2, 1]

numbers.pop() # Removes and returns the last element of the list
print(numbers) # Output: [9, 5, 10, 2]