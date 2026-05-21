#Write a program to find out whether a given post is taling about "Harry" or not.
# taking input from the user for the post   
post = input("Enter a post: ")
# checking if the post contains the word "Harry"    
if "Harry".lower() in post.lower():
    print("The post is talking about Harry.")   
else:
    print("The post is not talking about Harry.")