#Create an empty dictionary. Allow 4 friends to enter their favourite language as values and use their names as keys. Assume that the names are unique.
S = {} #This line initializes an empty dictionary called 'S'.

n1 = input("Enter name of friend 1: ")#This line prompts the user to enter the name of friend 1 and stores it in the variable 'n1'.
l1 = input("Enter favourite language of friend 1: ")#This line prompts the user to enter the favourite language of friend 1 and stores it in the variable 'l1'.
S[n1] = l1#This line adds a key-value pair to the dictionary 'S' where the key is the name of friend 1 (stored in 'n1') and the value is their favourite language (stored in 'l1').

n2 = input("Enter name of friend 2: ")#This line prompts the user to enter the name of friend 2 and stores it in the variable 'n2'.
l2 = input("Enter favourite language of friend 2: ")#This line prompts the user to enter the favourite language of friend 2 and stores it in the variable 'l2'.
S[n2] = l2#This line adds a key-value pair to the dictionary 'S' where the key is the name of friend 2 (stored in 'n2') and the value is their favourite language (stored in 'l2').             

n3 = input("Enter name of friend 3: ")  #This line prompts the user to enter the name of friend 3 and stores it in the variable 'n3'.   
l3 = input("Enter favourite language of friend 3: ")    #This line prompts the user to enter the favourite language of friend 3 and stores it in the variable 'l3'.
S[n3] = l3          #This line adds a key-value pair to the dictionary 'S' where the key is the name of friend 3 (stored in 'n3') and the value is their favourite language (stored in 'l3').

n4 = input("Enter name of friend 4: ")  #This line prompts the user to enter the name of friend 4 and stores it in the variable 'n4'.
l4 = input("Enter favourite language of friend 4: ")    #This line prompts the user to enter the favourite language of friend 4 and stores it in the variable 'l4'.
S[n4] = l4      

print(S) #This line prints the dictionary 'S'.