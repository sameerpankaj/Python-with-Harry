#Write a program to find the sum fo first n natural numbers using a while loop.
number = int(input("Enter a number: ")) # Get the number from the user



i = 1 # Initialize the counter variable to 1
total_sum = 0 # Initialize the variable to store the sum of natural numbers to 0
while i <= number: # Loop until the counter variable is less than or equal to the number
    total_sum += i # Add the current value of the counter variable to the total sum
    i += 1 # Increment the counter variable by 1 in each iteration  

print(total_sum) # Print the total sum
# For example, if the user enters 5, the output will be:
# The sum of the first 5 natural numbers is: 15
# This program calculates the sum of the first n natural numbers by using a while loop to iterate