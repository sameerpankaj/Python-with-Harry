'''
The __init__() constructor is a special method in Python that is automatically called when an object is created.

It is commonly used to initialize (set up) the object's attributes.

Basic Syntax
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

s1 = Student("Sameer", 25)

print(s1.name)
print(s1.age)

Output:

Sameer
25
How it works

When you write:

s1 = Student("Sameer", 25)

Python automatically calls:

Student.__init__(s1, "Sameer", 25)

Here:

self refers to the newly created object (s1).
name gets "Sameer".
age gets 25.
Constructor without parameters
class Employee:
    def __init__(self):
        print("Employee object created")

e1 = Employee()

Output:

Employee object created
Example with methods
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self.salary}")

e1 = Employee("Harry", 50000)
e1.show()

Output:

Name: Harry
Salary: 50000
Important points

The name must be exactly:

__init__

(double underscores before and after init).

self must be the first parameter for instance constructors.
You don't call __init__() directly in normal usage; it runs automatically when creating an object.
Simple way to remember

Think of __init__() as:

"The setup method that runs automatically when a new object is created."

'''

class Employee:
    language = 'Python'
    salary = 1200000

    def __init__(self):#dunder method which is automatically called
        #dunder method starts with underscore and ends with underscore
        print('I acm creating an object')

    def getInfo(self):
        print(f'The language is {self.language}. The salary is {self.salary}')

    @staticmethod
    def greet():
        print('Good morning')

harry = Employee()
harry.name = 'Harry'
print(harry.name, harry.salary)

rohan = Employee()
            