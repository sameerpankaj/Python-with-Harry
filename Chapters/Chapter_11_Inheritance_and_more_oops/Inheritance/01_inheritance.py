'''
Inheritance in Python

Inheritance is an Object-Oriented Programming (OOP) feature that allows one class (child/derived class) to acquire the properties and methods of another class (parent/base class).

Basic Syntax
class Parent:
    def greet(self):
        print("Hello from Parent")

class Child(Parent):
    pass

obj = Child()
obj.greet()

Output:

Hello from Parent

The Child class inherits the greet() method from the Parent class.

Example: Motorcycle
class Vehicle:
    def start(self):
        print("Vehicle started")

class Motorcycle(Vehicle):
    def ride(self):
        print("Motorcycle is riding")

bike = Motorcycle()

bike.start()  # Inherited method
bike.ride()   # Child's own method

Output:

Vehicle started
Motorcycle is riding
Constructor Inheritance
class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    pass

s = Student("Sameer")
print(s.name)

Output:

Sameer
Using super()

super() allows a child class to call methods from its parent class.

class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, roll_no):
        super().__init__(name)
        self.roll_no = roll_no

s = Student("Sameer", 101)

print(s.name)
print(s.roll_no)
Types of Inheritance in Python

Single Inheritance

Parent → Child

Multiple Inheritance

Parent1 + Parent2 → Child

Multilevel Inheritance

Grandparent → Parent → Child

Hierarchical Inheritance

        Parent
       /      \
   Child1   Child2
Hybrid Inheritance
Combination of two or more inheritance types.
Why Use Inheritance?
Reuse existing code.
Reduce duplication.
Make programs easier to maintain.
Create logical relationships between classes.

A simple definition to remember:

Inheritance is the mechanism by which a child class acquires the attributes and methods of a parent class, promoting code reusability and hierarchical relationships between classes.

'''

class Employee: #class definition
    company = 'ITC'#class variable    
    def show(self): #method definition. This is a method because it is defined inside a class
        print(f'The name is  {self.name} and the salary is {self.salary}')


class Programmer:
    company = 'ITC Infotech'
    def show(self):
       print(f'The name is {self.name} and the salarly is {self.salary}')


    def showLanguage(self):
       print(f'The name is {self.name} and he is good with {self.language} language')


a = Employee() #Object of Employee class
b = Programmer() #Object of Programmer class

print(a.company, b.company) #Accessing class variable





