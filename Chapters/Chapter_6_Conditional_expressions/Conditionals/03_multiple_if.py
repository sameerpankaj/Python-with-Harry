age = int(input("Enter your age: "))


#If statemet number 1. This is an independent if statement. It will be evaluated regardless of the other if statements.
if age%2 == 0:
    print("Your age is even.")
#This is the end of the first if statement. The next if statement will be evaluated regardless of the outcome of the first if statement.

#if statement number 2. This is an independent if statement. It will be evaluated regardless of the other if statements.    
if age > 45:
    print("You are middle-aged.")
#If statement number 3. This is a dependent if statement. It will only be evaluated if the first if statement is false.
elif age > 18:
    print("You are an adult.")
#If statement number 4. This is a dependent if statement. It will only be evaluated if the first and second if statements are false.
elif age > 12:
    print("You are a teenager.")
else:    #If statement number 5. This is a dependent if statement. It will only be evaluated if the first, second, and third if statements are false.
    print("You are a child.")


print("Thank you for using the age classifier.")


