#class method
#A class method is a method which is bound to the class and not the object of the class.
#@classmethod decorator is used to create a class method.
class Employee:
    a = 1
    @classmethod # this is a decorator which is used to create a class method. A decorator is a function which takes another function as an argument and extends the behaviour of that function without modifying it. In this case, the class method is extending the behaviour of the show method withoud modifying it.
    def show(cls):
        print(f'The class value of a is {cls.a}')

e = Employee()
e.a = 45


e.show() #This will print the value of a which is 1 because the class method is accessing the class variable a and not the instance variable a. If we want to access the instance variable a, we can use the instance method instead of the class method.