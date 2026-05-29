'''
a = 'a very long string with emails'

emails = []

a program is written and was run and the memeory was stored temporarily in RAM, after the program ends, the memory is empty

but if we want those memories to be stored permanently, than we can write them into files to persist the data

RAM = Random Access Memory-->Volatile
The random access memory is volatile and all its contents are lost once a program terminates
In order to persist the data forever, we use files.

A file is data stored in a storage device. A python program can talk to the file by reading content from 
it and writing content to it.


HDD = Non volatile 

Types fo files:
There are two types fo files:
1) Text files(.txt, .c etc)
2)Binary files (.jpg, .dat, etc)

Opening a File:
Python has an open() function for opening files. It takes 2 parameters: filename and made.



'''
f = open('file.txt') #Open is a built in function that helps to open a file in python
data = f.read() #f.read() is used to read the file
print(data)
f.close()#Once we open any file, we should always close it after the task is done.
#f.close helps to close the file