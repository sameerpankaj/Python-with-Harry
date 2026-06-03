'''
he finally block in Python is used to execute code no matter what happens in the try block—whether an exception occurs or not.

Basic Syntax
try:
    # Code that may raise an exception
finally:
    # Always runs
Example 1: No Exception
try:
    print("Inside try")
finally:
    print("Inside finally")

Output:

Inside try
Inside finally
Example 2: Exception Occurs
try:
    print(10 / 0)
finally:
    print("Inside finally")

Output:

Inside finally
ZeroDivisionError: division by zero

Notice that finally runs before the exception is propagated.

Example 3: try-except-finally
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except (ValueError, ZeroDivisionError):
    print("Invalid input or division by zero.")
finally:
    print("Execution completed.")

The finally block executes whether an exception occurs or not.

Common Use: Resource Cleanup
file = open("data.txt")

try:
    content = file.read()
    print(content)
finally:
    file.close()
    print("File closed.")

This ensures the file is closed even if an error occurs while reading it.

finally with return
def test():
    try:
        return "from try"
    finally:
        print("from finally")

print(test())

Output:

from finally
from try

The finally block runs before the function actually returns.

Execution Flow
No Exception
try → finally
Exception Not Handled
try → finally → exception propagates
Exception Handled
try → except → finally
Complete Structure
try:
    # risky code
except SomeError:
    # handle error
else:
    # runs if no exception
finally:
    # always runs
Key Point

Use finally for cleanup tasks such as:

Closing files
Closing database connections
Releasing locks
Cleaning up resources
'''

try:
    a = int(input('Hey, Enter a number:'))
    print(a)

except Exception as e: #except is same as catch in c or c++ or java
    print(e)

finally:
    print('I am inside finally')