#Write a program to find whether a given userbame contains less than 10 characters or not.
# taking input from the user for the username
username = input("Enter a username: ")  
# checking if the username contains less than 10 characters
if len(username) < 10:
    print("The username contains less than 10 characters.") 
else:
    print("The username contains 10 or more characters.")