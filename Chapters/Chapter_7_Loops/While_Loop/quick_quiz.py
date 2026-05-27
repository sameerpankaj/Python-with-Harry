#Write a program to print 1 to 50 using a while loop.
i = 1 #This line initializes the variable i with the value 1. This variable will be used as a counter in the while loop to keep track of how many times the loop has executed. Starting with 1 allows us to print numbers from 1 to 50 in the loop.
while i <= 50:#This line starts a while loop that will continue to execute as long as the condition i <= 50 is true. This means that the loop will run as long as the value of i is less than or equal to 50. Once i exceeds 50, the loop will stop executing.
    print(i)#   This line prints the current value of i to the console. Each time the loop runs, it will output the current value of i, which starts at 1 and increments with each iteration until it reaches 50.
    i += 1 # This line increments the value of i by 1 in each iteration of the loop. This is crucial to ensure that the loop eventually terminates. If we did not increment i, it would remain at 1 indefinitely, resulting in an infinite loop. By incrementing i, we allow it to eventually exceed 50, which will cause the loop to stop executing.

