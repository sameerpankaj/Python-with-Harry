#Write a program using functino to convert Celsius to Fahrenheit.
def celsius_to_fahrenheit(celsius): #function to convert Celsius to Fahrenheit
    fahrenheit = (celsius * 9/5) + 32 #formula to convert Celsius to Fahrenheit
    return fahrenheit #return the converted temperature in Fahrenheit
celsius = float(input("Enter temperature in Celsius: ")) #taking input from user for temperature in Celsius and converting it to float
result = celsius_to_fahrenheit(celsius) #calling the function celsius_to_fahrenheit with the input temperature and storing the result in a variable called result
print(f"{celsius} degrees Celsius is equal to {result} degrees Fahrenheit.") #printing the result to the user in a formatted string.    
    