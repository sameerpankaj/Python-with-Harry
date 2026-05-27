#Write a program to calculate the factorial of a given number using a for loop.

number = int(input("Enter a number: ")) # Get the number from the user
factorial = 1 # Initialize the variable to store the factorial result to 1
for i in range(1, number + 1): # Loop from 1 to the number
    factorial *= i # Multiply the current value of the counter variable to the factorial result
    #or factorial = factorial * i
print(f"The factorial of {number} is: {factorial}") # Print the factorial result   
# For example, if the user enters 5, the output will be:
# The factorial of 5 is: 120
# This program calculates the factorial of a given number by using a for loop to iterate through all
# the numbers from 1 to the given number and multiplying them together to get the final result.
