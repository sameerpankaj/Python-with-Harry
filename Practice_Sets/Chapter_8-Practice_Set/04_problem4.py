#Write a recursive function to calculate the sum of first n natural numbers.
def sum_of_natural_numbers(n): #function to calculate the sum of first n natural numbers
    if n == 1: #base case: if n is 1, return 1
        return 1
    else: #recursive case: return n plus the sum of the first n-1 natural numbers
        return n + sum_of_natural_numbers(n - 1)
    
n = int(input("Enter a positive integer: ")) #taking input from user for a positive integer and converting it to an integer
result = sum_of_natural_numbers(n) #calling the function sum_of_natural_numbers with the input integer and storing the result in a variable called result
print(f"The sum of the first {n} natural numbers is: {result}") #printing the result to the user in a formatted string.
