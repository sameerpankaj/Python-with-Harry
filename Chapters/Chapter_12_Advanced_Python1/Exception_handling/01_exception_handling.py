'''
Exception handling in Python is used to catch and handle errors that occur during program execution, preventing the program from crashing unexpectedly.

Basic Syntax
try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print(result)
except:
    print("An error occurred!")

If the user enters 0 or a non-numeric value, the program will print the error message instead of crashing.

Handling Specific Exceptions

It's better to catch specific exceptions rather than using a bare except.

try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ValueError:
    print("Please enter a valid integer.")
except ZeroDivisionError:
    print("You cannot divide by zero.")
Output Examples

Input:

0

Output:

You cannot divide by zero.

Input:

abc

Output:

Please enter a valid integer.
Using else

The else block runs only if no exception occurs.

try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ZeroDivisionError:
    print("Cannot divide by zero.")
else:
    print("Result:", result)
Using finally

The finally block always executes, whether an exception occurs or not.

try:
    file = open("data.txt")
    content = file.read()
except FileNotFoundError:
    print("File not found.")
finally:
    print("Execution completed.")

A common use is closing files or database connections.

Complete Example
try:
    num = int(input("Enter a number: "))
    result = 100 / num
except ValueError:
    print("Invalid input.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
else:
    print("Result:", result)
finally:
    print("Program ended.")
Raising Exceptions

You can create your own exceptions using raise.

age = -5

if age < 0:
    raise ValueError("Age cannot be negative.")

Output:

ValueError: Age cannot be negative.
Custom Exceptions
class InsufficientBalanceError(Exception):
    pass

balance = 100

withdraw = 150

if withdraw > balance:
    raise InsufficientBalanceError("Not enough balance.")
Common Python Exceptions
Exception	Description
ValueError	Invalid value (e.g., int("abc"))
TypeError	Wrong data type used
ZeroDivisionError	Division by zero
IndexError	Invalid list index
KeyError	Dictionary key not found
FileNotFoundError	File does not exist
AttributeError	Object has no such attribute
Exception Handling Flow
try
 ├─ No error → else → finally
 └─ Error → except → finally

This is the standard pattern you'll see in most Python programs:

try:
    # risky code
except SomeError:
    # handle error
else:
    # runs if no error
finally:
    # always runs

'''

try:
    a = int(input('Hey, Enter a number:'))
    print(a)

except Exception as e:
    print(e)

print('Thank you')