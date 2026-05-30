#Write a class 'Calculator' capable fo finding square, cube and square root of a number.
# Define a class named Calculator
class Calculator:

    # Constructor method that runs automatically when an object is created
    def __init__(self, n):

        # Store the value passed to the object in an instance variable named n
        self.n = n

    # Method to calculate and display the square of the number
    def square(self):

        # Multiply the number by itself and print the result
        print(f'The square is {self.n * self.n}')

    # Method to calculate and display the cube of the number
    def cube(self):

        # Multiply the number by itself three times and print the result
        print(f'The cube is {self.n * self.n * self.n}')

    # Method to calculate and display the square root of the number
    def squareroot(self):

        # Raise the number to the power of 1/2 (0.5) to get the square root
        print(f'The square root is {self.n ** (1/2)}')


# Create an object 'a' of the Calculator class and pass 4 to the constructor
a = Calculator(4)

# Call the square() method to print the square of 4
a.square()

# Call the cube() method to print the cube of 4
a.cube()

# Call the squareroot() method to print the square root of 4
a.squareroot()