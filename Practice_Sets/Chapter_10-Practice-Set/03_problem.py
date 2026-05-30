#Create a ckass with a class attribute a;create an object from ia nd set 'a' directly using objec.a=o.
#Does this chage the class attribute?

class Demo:
    a = 4

o = Demo()
print(o.a) #prints the class attribute because instance or object attribute is not present
o.a = 0#Instance attribute is set
print(o.a)#Prints the instance attribute because instance attribute is present now
print(Demo.a)#prints the class attributes

#The class attribute does not change