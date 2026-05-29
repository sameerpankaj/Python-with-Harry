#this program will append a string at the end of the file
#This will add the whole string after we run the program everytime

_string = 'Hey Harry, you are amazings'

f = open('my_file.txt', 'a') #this will create a file name with my_file.txt

f.write(_string)# this will write the value present in string to the file

f.close()