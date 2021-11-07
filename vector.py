class Vector:
    """A vector that takes in Cartesian coordinates"""

    def __init__(self, x, y):
        assert (isinstance(x, int) and isinstance(y, int)) or (isinstance(x, float) and isinstance(y, float)), 'Coordinates are not numbers'

        self.x = x
        self.y = y
    
    def __repr__(self):
        return f'Vector({self.x}, {self.y})'

    def __str__(self):
        return f'({self.x}, {self.y})'

class VectorOperations:
    """Vector operations"""

    def add(v1, v2):
        """Add vectors v1 and v2 (v1 + v2)"""

        assert isinstance(v1, Vector) and isinstance(v2, Vector)

        return Vector(v1.x + v2.x, v1.y + v2.y)
        
    def sub(v1, v2):
        """Subtract vectors v1 and v2 (v1 - v2)"""

        assert isinstance(v1, Vector) and isinstance(v2, Vector)

        return Vector(v1.x - v2.x, v1.y - v2.y)

    def mul_scalar(k, v):
        """Multiply vector v by scalar k (kv)"""

        assert (isinstance(k, int) or isinstance(k, float)) and isinstance(v, Vector)

        return Vector(k * v.x, k * v.y)
    
    def abs(v):
        """Find the magnitude of vector v (|v|)"""

        assert isinstance(v, Vector)

        return (v.x ** 2 + v.y ** 2) ** 0.5