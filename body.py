import matplotlib.pyplot as plt

from vertex import Vertex
from vector import Vector
from vector import VectorOperations as vec

class Body:
    """A physical body made of vertices and edges."""

    def __init__(self, vertices, edges=[], color='b'):
        assert len(vertices) > 2, 'Body is not two dimensional'
        for vertex in vertices:
            assert isinstance(vertex, Vertex), 'Not a list of vertices'
        for edge in edges:
            assert isinstance(edge, tuple) and isinstance(edge[0], int) and isinstance(edge[1], int) and len(edge) == 2, 'Not a list of edges'
            assert 0 <= edge[0] < len(vertices) and 0 <= edge[1] < len(vertices), 'Edge not in list of vertices'

        self.vertices = vertices
        self.mass = sum([vertex.mass for vertex in self.vertices])

        self.edges = edges if edges else list(zip(list(range(len(vertices))), list(range(1, len(vertices))) + [0]))

        self.color = color

        self.cm = Vertex(Vector(sum([vertex.mass * vertex.pos.x for vertex in self.vertices]) / self.mass,
                         sum([vertex.mass * vertex.pos.y for vertex in self.vertices]) / self.mass),
                         self.mass)
        
        self.moi = sum([vertex.mass * vec.abs(vec.sub(vertex.pos, self.cm.pos)) ** 0.5 for vertex in self.vertices])
    
    def draw(self, console=False):
        """Draw the body in Matplotlib or print in console"""

        if not console:
            x_coords, y_coords = [], []
            for i1, i2 in self.edges:
                self.draw_edge(self.vertices[i1].pos, self.vertices[i2].pos)
            self.draw_edge(self.vertices[-1].pos, self.vertices[0].pos)
        else:
            for edge in self.edges:
                print(f'{edge[0]} -- {edge[1]}')
    
    def draw_edge(self, v1, v2):
        """Draw edge from v1 to v2 in Matplotlib"""

        assert isinstance(v1, Vector) and isinstance(v2, Vector)

        plt.plot([v1.x, v2.x], [v1.y, v2.y], self.color)

    def __str__(self):
        string = f'Center of mass: {self.cm}, Total mass: {self.cm.mass}, Moment of inertia: {self.moi}\nEdges:'
        for i, j in self.edges:
            string += '\n'
            string += f'{self.vertices[i]} -- {self.vertices[j]}'
        return string
    
    def __repr__(self):
        return f'Body({[repr(vertex) for vertex in self.vertices]})'