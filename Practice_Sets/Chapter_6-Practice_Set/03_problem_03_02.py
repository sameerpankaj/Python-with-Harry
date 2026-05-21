#A spam comment is defined as a text containing following keywords: "make a lot of money", "buy now", "click this", "subscribe this". Write a program to detect these spams.
# taking input from the user for the comment
message = input("Enter a comment: ")
# defining the spam keywords
p1 = "make a lot of money"
p2 = "buy now"
p3 = "click this"
p4 = "subscribe this"   
# checking if the comment contains any of the spam keywords
if ((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)):
    print("This comment is a spam.")
else:
    print("This comment is not a spam.")