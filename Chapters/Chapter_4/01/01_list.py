#Python lists are containers that can hold a variety of data types, including integers, floats, strings, and even other lists. They are ordered, mutable (changeable), and allow duplicate elements. Lists are defined using square brackets [].    

friends = ["Apple", "Ornange", 5, 345.06, False,  "Charlie", "David"]

print(friends) # Output: ['Apple', 'Ornange', 5, 345.06, False, 'Charlie', 'David']
print(friends[0]) # Output: Apple
print(friends[1]) # Output: Ornange 

#Unlike strings which are immutable (cannot be changed), lists are mutable, meaning you can modify their contents after they have been created. You can change the value of an element in a list by accessing it using its index and assigning a new value to it.   
friends[0] = 'Grapes' # Modifying the first element of the list . 


print(friends[0]) # Output: 5