#Create a Class 'Programmer' for storing information of few programmers working at Microsoft.
class Programmer:
    comapny = 'Microsoft' #class attribute
    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin


p = Programmer('Harry', 1200000, 85057)
print(p.name, p.salary,p.pin, p.comapny)

r = Programmer('Rohan', 120000, 85057)
print(r.name, r.salary, r.pin, r.comapny)