def myFunc():
    print('Hello World')



if __name__ == '__main__':
    #if this code is directly executed by running the file it is present in
    print('We are directly running this code')
    myFunc()
    print(__name__) #here it will print __main__