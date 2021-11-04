class Vertex:
    def __init__(self, position, mass):
        """A vertex that is at a position coordinate with a given mass."""
        self.pos = position
        self.mass = mass
    
    def __repr__(self):
        return f'Vertex({self.pos}, {self.mass})'
    
    def __str__(self):
        return f'Coordinates: {repr(self)}, Mass: {self.mass}'
