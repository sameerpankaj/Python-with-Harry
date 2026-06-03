'''
The walrus operator in Python is written as := and was introduced in Python 3.8. Its official name is the assignment expression operator.

What it does

It lets you assign a value to a variable as part of an expression, instead of as a separate statement.

Basic example
# Without walrus operator
n = len("hello")
if n > 3:
    print(n)

# With walrus operator
if (n := len("hello")) > 3:
    print(n)
Why it’s useful

It avoids repeating calculations and can make code more concise—especially in loops and conditions.

Common use cases
1. In while loops
# Without walrus
line = input()
while line != "":
    print(line)
    line = input()

# With walrus
while (line := input()) != "":
    print(line)
2. Avoid recomputing values
# Without walrus
data = get_data()
if data:
    process(data)

# With walrus
if (data := get_data()):
    process(data)
Things to watch out for
Overusing it can make code harder to read.
It’s best used when it clearly reduces duplication.
You must use parentheses in many cases (like inside if conditions).
Quick summary
:= assigns and returns a value in one step
Helps write more compact code
Best used sparingly for clarity

'''

if (n := len([1, 2, 3, 4, 5])) > 3:
    print(f'List is too long ({n} elemnets, expected <=3)') 
    #Output : List is too long (5 elements, expected <=3)

    