class Vector:
    """A vector that takes in Cartesian coordinates"""
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return f'Vector({self.x}, {self.y})'

    def __str__(self):
        return f'({self.x}, {self.y})'

class VectorOperations:
    """Vector operations"""
    def add(self, v_1, v_2):
        return Vector(v_1.x + v_2.x, v_1.y + v_2.y)
        
    def sub(self, v_1, v_2):
        return Vector(v_1.x - v_2.x, v_1.y - v_2.y)

    def mul_scalar(self, k, v):
        return Vector(k * v.x, k * v.y)
    
    def abs(self, v):
        return (v.x ** 2 + v.y ** 2) ** 0.5