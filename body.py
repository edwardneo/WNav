import matplotlib.pyplot as plt

from vertex import Vertex
from vector import Vector
from vector import VectorOperations as vec

import time

class Body:
    """A physical body made of vertices and edges."""

    def __init__(self, vertices, trans_vel=Vector(0, 0), ang_vel=0, time_step=0.03):
        assert len(vertices) > 2, 'Body is not two dimensional'
        for vertex in vertices:
            assert isinstance(vertex, Vertex), 'Not a list of vertices'

        self.vertices = vertices
        self.mass = sum([vertex.mass for vertex in self.vertices])

        self.cm = Vertex(Vector(sum([vertex.mass * vertex.pos.x for vertex in self.vertices]) / self.mass,
                         sum([vertex.mass * vertex.pos.y for vertex in self.vertices]) / self.mass),
                         self.mass)
        
        self.moi = sum([vertex.mass * vec.abs(vec.sub(vertex.pos, self.cm.pos)) ** 0.5 for vertex in self.vertices])

        self.trans_vel = trans_vel
        self.ang_vel = ang_vel

        self.time_step = time_step
    
    def step(self):
        """Moves the body one frame forward"""
        
        displacement = vec.mul_scalar(self.time_step, self.trans_vel)

        for vertex in self.vertices:
            radial_axis = vec.sub(vertex.pos, self.cm.pos)
            new_radial_axis = vec.rotate(radial_axis, self.ang_vel * self.time_step)

            new_pos = vec.add(vec.add(self.cm.pos, displacement), new_radial_axis)

            vertex.set(new_pos)
        
        self.cm.pos = vec.add(self.cm.pos, displacement)
    
    def spin(self, torque):
        """Applies a torque for one frame"""

        self.ang_vel += torque / self.moi * self.time_step
    
    def set_data(self):
        """Gets the x and y values from the vertices"""

        return [vertex.pos.x for vertex in self.vertices] + [self.vertices[0].pos.x], [vertex.pos.y for vertex in self.vertices] + [self.vertices[0].pos.y]

    def display(self):
        """Display the vertices in the console"""

        while True:
            print(self.vertices)
            time.sleep(self.time_step)
            self.step()

    def __str__(self):
        string = f'Center of mass: {self.cm}, Total mass: {self.cm.mass}, Moment of inertia: {self.moi}\nEdges:'
        for i, j in self.edges:
            string += '\n'
            string += f'{self.vertices[i]} -- {self.vertices[j]}'
        return string
    
    def __repr__(self):
        return f'Body({[repr(vertex) for vertex in self.vertices]})'