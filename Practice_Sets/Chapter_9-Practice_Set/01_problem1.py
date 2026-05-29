#Write a program to read the text from a given file 'poems.txt' and find out 
#wheteher if contains the word 'twinkle'.

f = open('poem.txt')
content = f.read()

if ('twinkle' in content):
    print('Twinkle is present in the content')

else:
    print('The word twinkle is not present in the content')
f.close()