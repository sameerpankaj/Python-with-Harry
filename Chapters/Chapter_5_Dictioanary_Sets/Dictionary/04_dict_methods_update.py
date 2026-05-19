marks = {
    "Alice": 85, 
    "Bob": 90, 
    "Charlie": 78
    }

print(marks.update({"Alice": 92}))  # Updates the dictionary with the key-value pairs from another dictionary or from an iterable of key-value pairs
print(marks)  # The original dictionary is modified with the new key-value pair added
print(marks.get("Sameer"))  # Returns the value for the given key if it exists, otherwise returns the default value

print(marks.get("SameerPankaj"))  # This will return None because the key "SameerPankaj" does not exist in the dictionary, and we are using the get() method which returns None by default when the key is not found.
print(marks['Sameer']) # This will raise a KeyError because the key "Sameer" does not exist in the dictionary, and we are trying to access it directly without using the get() method which provides a default value.