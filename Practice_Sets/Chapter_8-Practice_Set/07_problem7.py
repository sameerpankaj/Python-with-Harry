#Write a python function to remove a given word from a list and strip it at the same time.
def remove_word_and_strip(word_list, word_to_remove): #function to remove a given word from a list and strip it at the same time
    stripped_word = word_to_remove.strip() #strip the word to remove
    if stripped_word in word_list: #check if the stripped word is in the list
        word_list.remove(stripped_word) #remove the stripped word from the list
    return word_list #return the modified list      
word_list = input("Enter a list of words separated by commas: ").split(',') #taking input from user for a list of words separated by commas and splitting it into a list
word_to_remove = input("Enter the word to remove: ") #taking input from user for the word to remove
result = remove_word_and_strip(word_list, word_to_remove) #calling the function remove_word_and_strip with the input list and word to remove and storing the result in a variable called result
print(f"The modified list after removing '{word_to_remove}' is: {result}") #printing the result to the user in a formatted string.
