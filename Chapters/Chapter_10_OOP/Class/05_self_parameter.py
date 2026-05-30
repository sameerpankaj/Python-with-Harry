'''
In Python, self refers to the current object (instance) of a class.

When you create an object and call one of its methods, Python automatically passes that object as the first argument to the method. By convention, we name this first parameter self.

Example
class Student:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, my name is {self.name}")

s1 = Student("Sameer")
s1.greet()

Output:

Hello, my name is Sameer
What's happening?

When you write:

s1.greet()

Python internally does something like:

Student.greet(s1)

So self refers to s1.

Why use self?

It lets each object store and access its own data.

class Dog:
    def __init__(self, name):
        self.name = name

dog1 = Dog("Tommy")
dog2 = Dog("Bruno")

print(dog1.name)
print(dog2.name)

Output:

Tommy
Bruno

Here, self.name keeps track of the name belonging to each specific dog.

Is self a keyword?

No. You could technically write:

class Test:
    def show(me):
        print("Hello")

But using self is the standard Python convention and is strongly recommended.

Simple way to remember

Think of self as:

"this object" or "the current object I'm working with."

When you're learning OOP, almost every instance method will start with:

def method_name(self):
    ...

because it needs access to the current object's attributes and methods.
'''


class Employee:
    language = 'Python'
    salary = 1200000

    def getInfo(self): #This function is created inside the class Employee
        print(f'The language is {self.language}. The salary is {self.salary} ')

    def greet(self):
        print('Good morning')

harry = Employee()
harry.language = 'Javascript'
print(harry.language, harry.salary)


harry.getInfo() #This works like: Employee.getInfo(Harry)
harry.greet()