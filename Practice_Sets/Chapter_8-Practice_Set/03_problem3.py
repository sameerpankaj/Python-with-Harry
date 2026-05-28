#How do you prevent a python print() function from printing a new line at the end of the output?
#You can prevent the print() function from printing a new line at the end of the output by using the end parameter. By default, the end parameter is set to '\n', which adds a new line after the output. To prevent this, you can set the end parameter to an empty string '' or any other character you want to use as a separator. For example:

print("Who are you?") # This will not add a new line after printing "Who are you?"
print("Hello, ", end='') # This will not add a new line after printing "Hello, "
print("world!") # This will print "world!" on the same line as "Hello, " because the end parameter in the previous print statement was set to an empty string.  
