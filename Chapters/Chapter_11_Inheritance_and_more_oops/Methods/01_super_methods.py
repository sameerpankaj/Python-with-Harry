#Multilevel Inheritance
class Employee: #Parent class
    def __init__(self):
         print('Constructor of Employee')
    a = 1

class Programmer(Employee):#This is the child class of the Employee class and the parent class of the class Manager
    def __init__(self):
         print('Constructor of Programmer')
    b = 2

class Manager(Programmer):#This is the child class of Programmer class and grand child class of Empployee class
    def __init__(self):
         super().__init__() #This will call the constructor of the parent class which is Programmer and then the constructor of Employee class will be called because the constructor of Programmer class is calling the constructor of Employee class using super()
         print('Constructor of Manager')
    c = 3



o = Manager()
print(o.a, o.b, o.c) #Prints the a attribute of the class Employee




# o = Programmer()
# print(o.a, o.b)

# o = Manager()
# print(o.a, o.b, o.c)