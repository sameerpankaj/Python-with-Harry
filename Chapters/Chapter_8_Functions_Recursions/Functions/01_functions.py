#A function is a block of code which only runs when it is called. You can pass data, known as parameters, into a function. A function can return data as a result.  
#Creating a Function
def my_function():
  print("Hello from a function")    
#Calling a Function
my_function()
#Information can be passed into functions as arguments. Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.
def my_function(fname):
  print(fname + " Refsnes")
my_function("Emil")
my_function("Tobias")   
my_function("Linus")
#If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition. This way the function will receive a tuple of arguments, and can access the items accordingly:
def my_function(*kids):
  print("The youngest child is " + kids[2])
my_function("Emil", "Tobias", "Linus")
    