#Write a program to create a dictionary of Hindi words with values as their English translation. Provide a user with an option to look it up!

words = {
    
    "Hello": "नमस्ते",
    "Thank you": "धन्यवाद",
    "Please": "कृपया"


}
word = input("Enter a Hindi word to look up its English translation: ")#This line prompts the user to enter a Hindi word and stores it in the variable 'word'. 
print(words[word]) #This line will print the English translation of the Hindi word entered by the user.