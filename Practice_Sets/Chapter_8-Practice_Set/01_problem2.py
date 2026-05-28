#Write a program using functions to find greatest of three numbers without user input.
def greatest_of_three(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c

# Example usage with predefined values
num1 = 10
num2 = 20
num3 = 15

#result = greatest_of_three(num1, num2, num3)
print(greatest_of_three(num1, num2, num3)) # Output: 20
#this print statement will call the function greatest_of_three with the predefined values num1, num2, and num3, and print the result which is the greatest of the three numbers.