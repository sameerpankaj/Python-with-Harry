#Write a program to find whether a given number is prime or not.
# Get the number from the user
number = int(input("Enter a number: "))
# Check if the number is less than 2
for i in range(2, number): # Loop from 2 to the number-1
    if number % i == 0:# Check if the number is divisible by any number in the range
        print(f"{number} is not a prime number.")# If the number is divisible by any number in the range, it is not a prime number
        break# If the number is not divisible by any number in the range, it is a prime number

else:# The else block is executed if the loop completes without finding any divisor, which means the number is prime
    print(f"{number} is a prime number.")# For example, if the user enters 7, the output will be:
# 7 is a prime number.
# If the user enters 10, the output will be:
# 10 is not a prime number.
        