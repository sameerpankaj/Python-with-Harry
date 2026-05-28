#Write a function which converts inches to cms
def inches_to_cms(inches): #function to convert inches to centimeters
    cms = inches * 2.54 #formula to convert inches to centimeters
    return cms #return the converted length in centimeters  
inches = float(input("Enter length in inches: ")) #taking input from user for length in inches and converting it to float
result = inches_to_cms(inches) #calling the function inches_to_cms with the input length and storing the result in a variable called result
print(f"{round(inches, 2)} inches is equal to {round(result, 2)} centimeters.") #printing the result to the user in a formatted string. 
#This print can be also written as: print(inches_to_cms(inches)) but the above format is more user-friendly.    
    