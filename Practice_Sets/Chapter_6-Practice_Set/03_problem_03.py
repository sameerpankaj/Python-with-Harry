#A spam comment is defined as a text containing following keywords: "make a lot of money", "buy now", "click this", "subscribe this". Write a program to detect these spams.
# taking input from the user for the comment
comment = input("Enter a comment: ")    
# defining the spam keywords
spam_keywords = ["make a lot of money", "buy now", "click this", "subscribe this"]
# checking if the comment contains any of the spam keywords
if any(keyword in comment for keyword in spam_keywords):
    print("This comment is a spam.")    

else:
    print("This comment is not a spam.")