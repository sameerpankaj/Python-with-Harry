#Write a python function to print multiplication table of a given number.
def multiplication_table(number): #function to print multiplication table of a given number 
    for i in range(1, 11): #loop to iterate from 1 to 10
        print(f"{number} x {i} = {number * i}") #print the multiplication result in a formatted string
number = int(input("Enter a number to print its multiplication table: ")) #taking input from user for a number and converting it to an integer
multiplication_table(number) #calling the function multiplication_table with the input number
    