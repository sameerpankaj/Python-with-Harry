'''
A static method in Python is a method that belongs to a class but does not need access to the instance (self) or the class (cls).

You create one using the @staticmethod decorator.

Example
class Calculator:
    @staticmethod
    def add(a, b):
        return a + b

print(Calculator.add(5, 3))

Output:

8
Why use a static method?

Use a static method when the function is related to the class but doesn't need any data from a specific object.

For example:

class Math:
    @staticmethod
    def square(n):
        return n * n

print(Math.square(4))

Output:

16
Instance Method vs Static Method
Instance Method (uses self)
class Student:
    def __init__(self, name):
        self.name = name

    def display(self):
        print(self.name)

Requires an object:

s = Student("Sameer")
s.display()
Static Method (no self)
class Student:
    @staticmethod
    def greet():
        print("Welcome!")

Can be called directly:

Student.greet()

Output:

Welcome!
Quick Comparison
Method Type	First Parameter	Decorator
Instance Method	self	None
Class Method	cls	@classmethod
Static Method	None	@staticmethod
Example from "Code With Harry" style
class Employee:
    company = "Microsoft"

    @staticmethod
    def greet():
        print("Good Morning!")

harry = Employee()
harry.greet()

Output:

Good Morning!

Notice that greet() doesn't use self because it doesn't need information about any specific employee.


'''
class Employee:
    language = 'Python'
    salary = 1200000

    def getInfo(self):
        print(f'The language is {self.language}. The salary is {self.salary}')


    @staticmethod #It does not require any property of object
    def greet(self):
        print('Good morning')

harry = Employee()
harry.getInfo()
