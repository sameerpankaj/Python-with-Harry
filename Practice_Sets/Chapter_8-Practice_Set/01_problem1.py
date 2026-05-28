#Write a program using functions to find greatest of three numbers with user input.

def greatest_of_three(a, b, c):#function to find greatest of three numbers
    if a > b and a > c: #if a is greater than both b and c, then a is the greatest
        return a #  return a as the greatest number
    elif b > a and b > c: # if b is greater than both a and c, then b is the greatest
        return b # return b as the greatest number
    else:# if c is greater than both a and b, then c is the greatest
        return c # return c as the greatest number
    
num1 = float(input("Enter first number: ")) #   taking input from user for first number and converting it to float
num2 = float(input("Enter second number: "))    # taking input from user for second number and converting it to float
num3 = float(input("Enter third number: "))# taking input from user for third number and converting it to float

result = greatest_of_three(num1, num2, num3)# calling the function greatest_of_three with the three numbers as arguments and storing the result in a variable called result
print("The greatest of the three numbers is:", result)# printing the result to the user