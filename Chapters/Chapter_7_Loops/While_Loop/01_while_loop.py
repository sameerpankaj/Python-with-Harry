#While loops are used to execute a block of code repeatedly as long as a certain condition is true.
# Syntax:   
# while condition:
#     # code block to be executed
# Example 1: Using a while loop to print numbers from 1 to 5
i = 1
while i <= 5:
    print(i)
    i += 1  # Incrementing the value of i to avoid an infinite loop
    #i += 1 is a shorthand for i = i + 1, which updates the value of i by adding 1 to its current value. This is essential for the loop to eventually terminate when i exceeds 5.   
# Example 2: Using a while loop to calculate the factorial of a number
number = 5 # You can change this value to calculate the factorial of a different number
factorial = 1# The factorial of a number n is the product of all positive integers less than or equal to n. For example, the factorial of 5 (denoted as 5!) is 5 * 4 * 3 * 2 * 1 = 120.
while number > 1:# The loop continues until number is greater than 1. When number becomes 1, the loop will stop, and the factorial will have been calculated.
    factorial *= number# The current value of factorial is multiplied by number, and the result is stored back in factorial. This effectively accumulates the product of all integers from number down to 1.
    number -= 1# The value of number is decremented by 1 in each iteration, moving towards the base case where number becomes 1. This ensures that the loop will eventually terminate.
print(factorial)  # Output: 120
# Example 3: Using a while loop to create a simple menu-driven program  
choice = ""
while choice != "exit":
    print("Menu:")
    print("1. Option 1")
    print("2. Option 2")
    print("3. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        print("You selected Option 1")
    elif choice == "2":
        print("You selected Option 2")
    elif choice == "3":
        print("Exiting the program...")
    else:
        print("Invalid choice, please try again.")