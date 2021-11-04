from vertex import Vertex
from vector import VectorOperations as vec

class Body:
    """A physical body made of vertices and edges."""
    def __init__(self, vertices, edges=[]):
        assert len(vertices) > 2

        self.vertices = vertices
        self.mass = sum([vertex.mass for vertex in self.vertices])

        self.edges = edges if edges else zip(list(range(len(vertices))), list(range(1, len(vertices))) + [0])

        self.cm = Vertex(sum([vertex.mass * vertex.pos[0] for vertex in self.vertices]) / self.mass,
                         sum([vertex.mass * vertex.pos[1] for vertex in self.vertices]) / self.mass,
                         self.mass)
        
        self.moi = sum([vertex.mass * vec.abs(vec.sub(vertex.pos, self.cm)) ** 0.5 for vertex in self.vertices])
    
    def draw(self):
        for edge in self.edges:
            print(f'{edge[0]} -- {edge[1]}')

    def __str__(self):
        string = f'Center of mass: {self.cm}, Total mass: {self.cm.mass}, Moment of inertia: {self.moi}\nEdges:'
        for i, j in self.edges:
            string += '\n'
            string += f'{self.vertices[i]} -- {self.vertices[j]}'
        return string
    
    def __repr__(self):
        return f'Body({[repr(point) for point in self.points]})'