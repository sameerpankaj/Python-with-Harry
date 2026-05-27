#Write a program to print the multiplication table of a given number using for loop.

# Get the number from the user
number = int(input("Enter a number: "))


# Print the multiplication table
for i in range(1, 11):# Loop from 1 to 10
    print(f"{number} x {i} = {number * i}")# Print the multiplication result
    # The f-string is used to format the output in a readable way.
    # For example, if the user enters 5, the output will be:
    # 5 x 1 = 5
    # 5 x 2 = 10
    # and so on, up to 5 x 10 = 50.
    # This program allows the user to easily see the multiplication table for any number they choose. 
