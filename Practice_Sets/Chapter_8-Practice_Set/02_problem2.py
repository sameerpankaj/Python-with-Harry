#Write a program using function to convert fahrenheit to Celsius.
def fahrenheit_to_celsius(fahrenheit): #function to convert Fahrenheit to Celsius
    celsius = (fahrenheit - 32) * 5/9 #formula to convert Fahrenheit to Celsius
    return celsius #return the converted temperature in Celsius
fahrenheit = float(input("Enter temperature in Fahrenheit: ")) #taking input from user for temperature in Fahrenheit and converting it to float
result = fahrenheit_to_celsius(fahrenheit) #calling the function fahrenheit_to_celsius with the input temperature and storing the result in a variable called result
print(f"{round(fahrenheit, 2)} degrees Fahrenheit is equal to {round(result, 2)} degrees Celsius.") #printing the result to the user in a formatted string.
#This print can be also written as: print(fahrenheit_to_celsius(fahrenheit)) but the above format is more user-friendly.