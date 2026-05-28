#functions with arguments
def greet(name): #name is the parameter
    print("Hello, " + name + "!")   #name is the argument passed to the function
greet("Alice")#greet("Alice")  # Output: Hello, Alice!
greet("Bob")#greet("Bob")  # Output: Hello, Bob!


#function with multiple arguments
def add_numbers(a, b): #a and b are parameters
    return a + b
result = add_numbers(5, 3) #5 and 3 are arguments
print("The sum is:", result) #Output: The sum is: 8


#function with default argument
def greet(name="Guest"): #name is a parameter with a default value of "Guest"
    print("Hello, " + name + "!")#greet()  # Output: Hello, Guest!
greet()  # Uses default argument
greet("Alice")  # Overrides default argument


#function with variable number of arguments
def sum_all(*args):#*args allows the function to accept a variable number of arguments
    total = 0 #Initialize total to 0
    for num in args:#   
        total += num #Add each number in args to total
    return total #Return the total sum of all arguments
result = sum_all(1, 2, 3, 4) #Call the function with multiple arguments
print("The total sum is:", result) #Output: The total sum is: 10
