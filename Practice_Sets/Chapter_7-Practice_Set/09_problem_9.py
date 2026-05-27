#Write a program to print the following pattern:
'''

* * *
* *
* * * for n = 3

'''

''' 
n = int(input("Enter the number of rows: ")) # Get the number of rows from the user
for i in range(1, n + 1):# Loop through each row
    if (i == 1 or i == n):# Check if the current row is the first or last row
        print("*"* n, end="")# Print the first and last row with the required number of stars
    else:
        print('*', end="")
        print(" "* (n - 2), end="")
        print("*", end="")

print( )    # Print a new line after each row is printed

'''

n = int(input("Enter the number of rows: "))

for i in range(1, n + 1):

    if (i == 1 or i == n):
        print("*" * n, end="")
    else:
        print('*', end="")
        print(" " * (n - 2), end="")
        print("*", end="")

    print()   # New line after every row