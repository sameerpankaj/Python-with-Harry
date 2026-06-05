#Write a program to filter a list of numbers which are divisible by 5.

def divisible5(n):
    if(n%5 == 0):
        return True
    return False

a = [1, 2, 333, 444, 555, 8888, 5555, 3333, 5555, 333, 44]

f = list(filter(divisible5, a))

print(f)
