#Multilevel Inheritance
class Employee: #Parent class
    a = 1

class Programmer(Employee):#This is the child class of the Employee class and the parent class of the class Manager
    b = 2

class Manager(Programmer):#This is the child class of Programmer class and grand child class of Empployee class
    c = 3



o = Employee()
print(o.a) #Prints the a attribute of the class Employee
#print(o.b) #This will give an error because the object o is of class Employee and the attribute b is not present in the Employee class

o = Programmer()
print(o.a, o.b)

o = Manager()
print(o.a, o.b, o.c)