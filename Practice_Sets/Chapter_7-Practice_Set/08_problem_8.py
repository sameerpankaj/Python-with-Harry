#Write a program to pring the following pattern:
'''
*
* *      
* * *  for n = 3

'''
number = int(input("Enter the number of rows: ")) # Get the number of rows from the user
for i in range(1, number + 1):# Loop through each row
    for j in range(i):# Loop to print stars in the required pattern
        print("*", end=" ")# Print a star followed by a space without moving to the next line
    
    # Move to the next line
    print()# Print a new line after each row is printed     
