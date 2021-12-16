import numpy as np

from body import Body
from vertex import Vertex
from vector import Vector
from vector import VectorOperations as vec

class Circle(Body):
    def __init__(self, radius=1, pts=100, trans_vel=Vector(0, 0), ang_vel=0, time_step=0.03):
        vertices = []

        x_hat = Vector(radius, 0)

        for i in range(pts):
            vertices.append(Vertex(vec.rotate(x_hat, i / pts * 2 * np.pi), 1))
        
        super().__init__(vertices, trans_vel, ang_vel, time_step)

class Square(Body):
    def __init__(self, side=1, trans_vel=Vector(0, 0), ang_vel=0, time_step=0.03):
        vectors = [Vector(side / 2, side / 2),
                   Vector(-side / 2, side / 2),
                   Vector(-side / 2, -side / 2),
                   Vector(side / 2, -side / 2)]
        
        vertices = [Vertex(vector, 1) for vector in vectors]
        
        super().__init__(vertices, trans_vel, ang_vel, time_step)

class WeightedSquare(Body):
    def __init__(self, side=1, weights=[3, 2, 1, 1], trans_vel=Vector(0, 0), ang_vel=0, time_step=0.03):
        vertices = [Vertex(Vector(side / 2, side / 2), weights[0]),
                    Vertex(Vector(-side / 2, side / 2), weights[1]),
                    Vertex(Vector(-side / 2, -side / 2), weights[2]),
                    Vertex(Vector(side / 2, -side / 2), weights[3])]
        
        super().__init__(vertices, trans_vel, ang_vel, time_step)