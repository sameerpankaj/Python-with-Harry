#Write a program to find the greatest of four numbers entered by the user.
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))
d = int(input("Enter the fourth number: "))

if a > b and a > c and a > d:#  if a is greater than b, c and d then print a as greatest number
    print("The greatest number is:", a)
elif b > c and b > d:# if b is greater than c and d then print b as greatest number
    print("The greatest number is:", b)
elif c > d:# if c is greater than d then print c as greatest number
    print("The greatest number is:", c)
else:# if none of the above conditions are true then print d as greatest number
    print("The greatest number is:", d)