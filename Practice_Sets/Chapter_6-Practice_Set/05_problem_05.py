#Write a program which finds out whether a given name is present in a list or not.  
# taking input from the user for the name to search
name_to_search = input("Enter a name to search: ")      
# defining a list of names
names_list = ["Alice", "Bob", "Charlie", "David", "Eve"]    
# checking if the name is present in the list
if name_to_search in names_list:
    print(f"{name_to_search} is present in the .")
else:
    print(f"{name_to_search} is not present in the list.")
