#Exercise to understand the operator overloading concept

class Vector:
    def __init__(self, i, j):
        self.i = i
        self.j = j
    
    def __add__(self, input):
        return Vector(self.i + input.i, self.j + input.j)

    def __sub__(self, input):
        return Vector(self.i - input.i, self.j - input.j)

    def __mul__(self, input):
        return Vector(self.i * input.i, self.j * input.j)

    def __str__(self):
        return f"Vector({self.i}, {self.j})"
    
v1 = Vector(4,5)
v2 = Vector(-5,6)

print(v1+v2)
print(v1-v2)
print(v1*v2)