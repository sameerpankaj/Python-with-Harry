'''
In Python, the else block in a try statement runs only if no exception is raised in the try block.

Syntax
try:
    # Code that may raise an exception
except SomeException:
    # Handle the exception
else:
    # Runs only if no exception occurred
Example 1
try:
    num = int(input("Enter a number: "))
except ValueError:
    print("Invalid input!")
else:
    print("You entered:", num)
Input:
42

Output:

You entered: 42
Input:
abc

Output:

Invalid input!

Notice that the else block does not run when an exception occurs.

Why use else?

It helps separate:

Code that might fail → inside try
Code that should run only if the try succeeded → inside else

Example:

try:
    file = open("data.txt")
except FileNotFoundError:
    print("File not found.")
else:
    content = file.read()
    print(content)
    file.close()

Here, file.read() is only attempted if the file was opened successfully.

try + except + else + finally
try:
    num = int(input("Enter a number: "))
except ValueError:
    print("Please enter a valid integer.")
else:
    print("Square:", num ** 2)
finally:
    print("Program finished.")
If input is 5:
Square: 25
Program finished.
If input is abc:
Please enter a valid integer.
Program finished.
Flow
try
 ├─ Exception occurs? ── Yes ──► except ──► finally
 │
 └─ No exception ──────► else ───► finally


'''

try:
    a = int(input('Hey, Enter a number:'))
    print(a)



except Exception as e: #except is same as catch in c or c++ or java
    print(e)

else:
    print('I am inside else')

