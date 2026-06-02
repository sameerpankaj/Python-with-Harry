#Override the __len__() method on vector of problem 5 to display the dimension of the vector.

class Vector:
    def __init__(self, l):
        self.l = l
         

    # def __add__(self, other):
    #     result = Vector(self.x + other.x, self.y + other.y, self.z + other.z)
    #     return result
    
    # def __mul__(self, other):
    #     result = self.x * other.x + self.y * other.y + self.z * other.z
    #     return result
    
    # def __str__(self):
    #     return f'Vector({self.x}, {self.y}, {self.z})'
    
    def __len__(self):
        return len(self.l)
    

#Test the implementation
v1 = Vector([1, 2, 3])
print(len(v1))

# v2 = Vector(4, 5, 6)
# v3 = Vector(7, 8, 9) # Same dimension vector

# print(v1 + v2) # Output: Vector (5, 7, 9)
# print(v1 * v2) # Output: Vector ()

# print(v1 + v3) # Output: Vector (8, 10, 12)
# print(v1 * v3)