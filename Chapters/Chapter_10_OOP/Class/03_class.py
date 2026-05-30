

class Employee:
    language = 'Py' #This is a class attribute
    Salary = 1200000

harry = Employee()
harry.name = 'Harry' #This is an object or instance attribute
print(harry.name, harry.Salary, harry.language)

rohan = Employee()
rohan.name = 'Rohan Roro Robinson'#This is an object or instance attribute
print(rohan.name, rohan.language, rohan.Salary)

#Here name is object or instance attribute and Salary, language are class attributes as they directly belong to the class