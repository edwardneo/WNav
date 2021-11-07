from vector import Vector

class Vertex:
    """A vertex that is at a position coordinate with a given mass."""

    def __init__(self, position, mass):
        assert isinstance(position, Vector), 'Position is not vector'
        assert isinstance(mass, int) or isinstance(mass, float), 'Mass is not number'

        self.pos = position
        self.mass = mass
    
    def __repr__(self):
        return f'Vertex({self.pos}, {self.mass})'
    
    def __str__(self):
        return f'Coordinates: {repr(self)}, Mass: {self.mass}'
