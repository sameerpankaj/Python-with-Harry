#this program will write a string in file

_string = 'Hey Harry, you are amazing'

f = open('my_file.txt', 'w') #this will create a file name with my_file.txt

f.write(_string)# this will write the value present in string to the file

f.close()