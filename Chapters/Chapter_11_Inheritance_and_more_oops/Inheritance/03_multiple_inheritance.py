#Multiple inheritance

class Employee: #This is the 1st parent class
    company = 'ITC'
    name = 'Default Name'
    def show(self):
        print(f'The name of the Employeee is {self.name} and the company is {self.company}')


class Coder: #This is the second parent class
    language = 'Python'
    def printLanguages(self):
        print(f'Out of all the languages, here is your language {self.language}')



class Programmer(Employee, Coder): #Derivated Class or child class
    company ='ITC Infotech'
    def showLanguage(self):
        print(f'The name is {self.company} and he is good with {self.language} langugage')



a = Employee()
b = Programmer()

b.show()
b.showLanguage()
b.printLanguages()


#print(a.company, b.langugae)
