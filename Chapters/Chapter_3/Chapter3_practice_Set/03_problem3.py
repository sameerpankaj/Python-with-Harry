#Write a program to detect double space in a string
name = 'Harry is a good  boy and  '

print(name.find('  '))
print(name.find('Harry')) #This will return the index of Harry, that is 0

print(name) #Strings are immutable, which means that you cannnot change them by running functions on them

#if the output shows -1,that means there are no double spaces