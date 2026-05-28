#Recursion is a programming technique where a function calls itself in order to solve a problem. It typically involves a base case that stops the recursion and a recursive case that breaks the problem into smaller subproblems.  
#Example: Factorial of a number using recursion
def factorial(n): #Function to calculate factorial of a number
    if n == 1 or n == 0:  # Base case: factorial of 0 is 1
        return 1 # Recursive case: factorial of n is n multiplied by factorial of (n-1)
    else:
        return n * factorial(n - 1)  # Recursive case: n! = n * (n-1)!
    
n = int(input("Enter a number to calculate its factorial: "))  # Taking input from user
print(f"The factorial of {n} is: {factorial(n)}")  # Printing the result