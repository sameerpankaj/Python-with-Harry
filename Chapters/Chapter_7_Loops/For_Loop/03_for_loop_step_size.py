#step size in for loop
# In a for loop, the step size determines how much the loop variable is incremented (or decremented) in each iteration. By default, the step size is 1, which means that the loop variable will be incremented by 1 in each iteration. However, you can specify a different step size using the range() function in Python.
# The syntax for using a step size in a for loop is as follows: 
# for variable in range(start, stop, step):
# - start: The value at which the loop starts (inclusive). If not specified, it defaults to 0.
# - stop: The value at which the loop stops (exclusive). This is a required argument.
# - step: The value by which the loop variable is incremented (or decremented) in each iteration. If not specified, it defaults to 1.
# For example, if you want to print even numbers from 0 to 10, you can use a step size of 2 in the range() function like this:  
for i in range(0, 11, 2):
    print(i)
# In this example, the loop starts at 0, stops before 11, and increments by 2 in each iteration. Therefore, it will print the even numbers: 0, 2, 4, 6, 8, and 10.  
    