#Write a class 'Complex' to represent complex numbers, along with overloaded operators '+' and '*' which adds and multiplies them.

class Complex:
    def __init__(self, real, imagenary):
        self.real = real
        self.imagenary = imagenary

    def __add__(self, c2):
        return Complex(self.real + c2.real, self.imagenary * c2.imagenary)
    

    def __mul__(self, c2):
        return Complex(
            self.real * c2.real - self.imagenary * c2.imagenary,
            self.real * c2.imagenary + self.imagenary * c2.real
        )

    
    def __str__(self):
        return f'{self.real} + {self.imagenary}i'
    

c1 = Complex(1, 2)
c2 = Complex(3, 4)

print(c1 + c2)
print(c1 * c2)
