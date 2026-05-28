#we can have a value as default as default argument in function.

#If we specify name = 'stranger' in the line conatining def, this value is used when no argument is passed.

def goodDay(name, ending = 'Thank you!'):
    print(f"Good day, {name}!")
    print(ending)

goodDay("Harry") #Output: Good day, Harry!
goodDay("Harry", "Have a great day!") #Output: Good day, Harry! Have a great day!