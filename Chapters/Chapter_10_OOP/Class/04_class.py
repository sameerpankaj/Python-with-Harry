#instance or object vs class attributes

#Note: Instance or object attributes take preferences over class attributes during assignment and retrieval.
#In this example we have a class attribute with the name language and we have an instance or object attribute
#with language as well. so in output, instance attribute will have preference
#Javascript will be the output for language

class Employee:
    language = 'Python'#This is a class attribute
    salary = 120000


harry = Employee()
harry.language = 'Javascript' #This is an instance or object attribute
print(harry.language, harry.salary)


