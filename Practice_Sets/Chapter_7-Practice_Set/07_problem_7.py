#Write a program to print the following pattern:
'''
    *
  * * *
* * * * * for n = 3

'''

number = int(input("Enter the number of rows: ")) # Get the number of rows from the user
for i in range(1, number + 1):# Loop through each row
#it works by first printing the required number of spaces to align the stars in the center, and then printing the stars in the required pattern. The number of spaces decreases as we move down the rows, while the number of stars increases.

    # Print spaces
    for j in range(number - i):# Loop to print spaces before the stars
        print(" ", end="")# Print a space without moving to the next line
    
    # Print stars
    for k in range(2 * i - 1):# Loop to print stars in the required pattern
        print("*", end="")# Print a star without moving to the next line
    
    # Move to the next line
    print()# Print a new line after each row is printed  