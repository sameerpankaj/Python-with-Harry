class Employee:
    language = 'Python'
    salary = 1200000

    def __init__(self, name, salary, language):#dunder method which is automatically called
        #dunder method starts with underscore and ends with underscore
        self.name = name
        self.salary = salary
        self.language = language
        print('I acm creating an object')

    def getInfo(self):
        print(f'The language is {self.language}. The salary is {self.salary}')

    @staticmethod
    def greet():
        print('Good morning')

harry = Employee('Harry', 1300000, 'Javascript')
#harry.name = 'Harry'
print(harry.name, harry.salary, harry.language)

#rohan = Employee()