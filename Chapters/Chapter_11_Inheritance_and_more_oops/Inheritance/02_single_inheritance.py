
#Single Inheritance
class Employee: #Parent class
    company = 'ITC'
    def show(self):
        print(f'The name of the Employee is {self.name} and the salary is {self.salary}')

class Programmer(Employee): #Programmer is the child class and Employee is the parent class. Programmer inherits from Employee
    company = 'ITC Infotech'
    def showLanguage(self):
        print(f'The name is {self.name} and he is good with {self.language} langugae')


a = Employee()
b = Programmer()

print(a.company, b.company) #accessing class variable of Employee class and Programmer class. This is an example of single inheritance.