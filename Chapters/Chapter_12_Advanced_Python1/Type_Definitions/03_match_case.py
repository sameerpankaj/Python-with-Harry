'''
match-case is Python's structural pattern matching feature, introduced in Python 3.10. It works somewhat like a switch statement in other languages, but is much more powerful.

Basic Syntax
day = 3

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case _:
        print("Invalid day")

Output:

Wednesday

The _ acts as a default case.

Matching Strings
command = "start"

match command:
    case "start":
        print("Starting...")
    case "stop":
        print("Stopping...")
    case _:
        print("Unknown command")
Multiple Values in One Case
grade = "B"

match grade:
    case "A" | "B":
        print("Good job!")
    case "C":
        print("Passed")
    case _:
        print("Try again")

Output:

Good job!
Matching Lists or Tuples
point = (0, 5)

match point:
    case (0, y):
        print(f"On Y-axis at {y}")
    case (x, 0):
        print(f"On X-axis at {x}")
    case (x, y):
        print(f"Point is ({x}, {y})")

Output:

On Y-axis at 5
Using Conditions (Guards)
age = 20

match age:
    case x if x >= 18:
        print("Adult")
    case _:
        print("Minor")
Matching Dictionaries
person = {"name": "Sameer", "age": 25}

match person:
    case {"name": name, "age": age}:
        print(f"{name} is {age} years old")

Output:

Sameer is 25 years old
When to Use match-case

Good for:

Menu systems
Command parsing
Processing structured data (lists, tuples, dictionaries)
Replacing long if-elif-else chains

Example:

choice = input("Enter operation: ")

match choice:
    case "add":
        print("Adding")
    case "delete":
        print("Deleting")
    case "update":
        print("Updating")
    case _:
        print("Invalid operation")
Comparison
# if-elif
if command == "start":
    ...
elif command == "stop":
    ...
else:
    ...

# match-case
match command:
    case "start":
        ...
    case "stop":
        ...
    case _:
        ...

match-case becomes especially useful when matching complex patterns like tuples, lists, and dictionaries, where it is much cleaner than nested if statements.


'''

def http_status(status):
    match status:
        case 200:
            return 'OK'
        case 404:
            return 'Not found'
        case 500:
            return 'Internal Server Error'
        case _:
            return  'Unknown status'

#Usage    
print(http_status(200))#Output: OK 
print(http_status(404))#Output: Not found 
print(http_status(500))#Output: Internal Server
print(http_status(5007))#Output: Unknown status: if the number is not available in the program, it will print unknown status
