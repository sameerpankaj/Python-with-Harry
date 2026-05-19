#Write a program to input eight numbers from the user and display all the unique numbers (once).

s = set() #'This line initializes an empty set called 's' to store unique numbers.
n = input("Enter number 1: ") 
s.add(int(n)) #This line adds the first number entered by the user to the set 's'.
n = input("Enter number 2: ")   
s.add(int(n)) #This line adds the second number entered by the user to the set 's'.
n = input("Enter number 3: ")
s.add(int(n)) #This line adds the third number entered by the user to the set 's'.
n = input("Enter number 4: ")
s.add(int(n)) #This line adds the fourth number entered by the user to the set 's'.
n = input("Enter number 5: ")
s.add(int(n)) #This line adds the fifth number entered by the user to the set 's'.
n = input("Enter number 6: ")
s.add(int(n)) #This line adds the sixth number entered by the user to the set 's'.
n = input("Enter number 7: ")
s.add(int(n)) #This line adds the seventh number entered by the user to the set 's'.
n = input("Enter number 8: ")
s.add(int(n))    #This line adds the eighth number entered by the user to the set 's'.
print("Unique numbers entered:", s) #This line prints the unique numbers entered by the user