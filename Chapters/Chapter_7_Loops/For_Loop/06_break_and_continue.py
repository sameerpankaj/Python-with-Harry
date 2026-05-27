#break and continue statement in for loop
for i in range(100):
    if(i == 50): # This line checks if the current value of i is equal to 50. If this condition is true, it will execute the block of code inside the if statement.
        break # This line will exit the for loop immediately when i is equal to 50. The break statement is used to terminate the loop prematurely, so the loop will not continue to iterate through the remaining numbers after 50.
    print(i) # This line prints the current value of i to the console. Each time the loop runs, it will output the current number that i is representing, starting from 0 and going up to 99.