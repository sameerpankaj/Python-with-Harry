# This program demonstrates the use of elif statements to handle multiple conditions.
#if elif else ladder

a = int(input("Enter your age: "))

if a >= 18:
    print("You are an adult.")   
    print("You can vote and drive.")

elif a < 0:
    print("Invalid age. Age cannot be negative.")

elif a == 0:
    print("You are a newborn. Welcome to the world!")   

else:
    print("You are a minor.")
    print("You cannot vote or drive.")

print('End of program.  ')
