#Write a function to print first n lines fo the following pattern:
'''
***
**
*
for n = 3

'''

def print_pattern(n): #function to print the pattern
    for i in range(n, 0, -1): #loop to iterate from n to 1
        print('*' * i) #print '*' i times
n = int(input("Enter the number of lines for the pattern: ")) #taking input from user for the number of lines and converting it to an integer
print_pattern(n) #calling the function print_pattern with the input number of lines 
    