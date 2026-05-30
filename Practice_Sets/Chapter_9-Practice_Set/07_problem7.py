#Write a program to find out the line number where python is present from question 6.

line = 1

with open('log.txt') as f:
    lines = f.readlines()


linenumber = 1
for line in lines:
    if('Python' in line):
        print(f'Yes Python is present in line number: {linenumber}')
        break
    linenumber += 1

else:
    print('No Python is not present')