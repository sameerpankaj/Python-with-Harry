#Write a program to print the multiplication table of a given number using a while loop.

number = int(input("Enter a number: ")) # Get the number from the user

i = 1 # Initialize the counter variable to 1
while i < 11:# Loop until the counter variable is less than 11
    print(f"{number} x {i} = {number * i}")# Print the multiplication result
    # The f-string is used to format the output in a readable way.
    i += 1  # Increment the counter variable by 1 in each iteration
# For example, if the user enters 5, the output will be:
# 5 x 1 = 5
# 5 x 2 = 10    
# and so on, up to 5 x 10 = 50.
# This program allows the user to easily see the multiplication table for any number they choose using a while loop instead of a for loop.
    