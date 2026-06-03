'''
A global variable in Python is a variable that is defined outside any function and can be accessed from anywhere in the program.

Basic Example
x = 10  # Global variable

def show():
    print(x)

show()
print(x)

Output:

10
10

The function can read the global variable x.

Modifying a Global Variable

If you try to modify a global variable inside a function without using global, Python creates a new local variable instead.

Incorrect
x = 10

def update():
    x = 20  # Local variable
    print(x)

update()
print(x)

Output:

20
10

The global x remains unchanged.

Using the global Keyword

To modify a global variable inside a function, use global.

x = 10

def update():
    global x
    x = 20

update()
print(x)

Output:

20

Now the function updates the global variable.

Multiple Global Variables
count = 0
name = "Sameer"

def update():
    global count, name
    count += 1
    name = "Alex"

update()

print(count)
print(name)

Output:

1
Alex
Reading vs Writing
Reading a global variable
x = 100

def show():
    print(x)

show()

No global keyword is needed.

Writing to a global variable
x = 100

def change():
    global x
    x = 200

change()

global is required.

Global vs Local Variables
x = 10  # Global

def test():
    x = 20  # Local
    print("Local:", x)

test()
print("Global:", x)

Output:

Local: 20
Global: 10

The local variable shadows the global one inside the function.

Best Practice

While global is useful, excessive use can make code harder to understand and maintain.

Instead of:

count = 0

def increment():
    global count
    count += 1

Prefer:

def increment(count):
    return count + 1

count = increment(count)

This makes the function easier to test and reuse.

Summary
Action	Need global?
Read a global variable	No
Modify a global variable	Yes
Create a local variable with the same name	No
global variable_name

Use global only when you truly need a function to modify a variable defined outside the function.
'''

a = 89
def fun():
    #local a
    a = 3

    print(a)

fun()