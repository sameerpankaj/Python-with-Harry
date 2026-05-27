#Write a program to print the multiplication tbale of n using for loops in reverse order:
n = int(input("Enter the number for which you want to print the multiplication table: ")) # Get the number from the user
print(f"Multiplication table of {n} in reverse order:") # Print the header
for i in range(10, 0, -1):# Loop from 10 to 1 in reverse order
    print(f"{n} x {i} = {n * i}")# Print the multiplication result for each iteration

    '''
    or

n = int(input("Enter the number for which you want to print the multiplication table: "))
print(f"Multiplication table of {n} in reverse order:")
for i in range(1, 11):
    print(f"{n} x {11 - i} = {n * (11 - i)}")


    
    '''
