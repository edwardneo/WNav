import matplotlib.pyplot as plt

from body import Body
from vertex import Vertex
from vector import Vector
from vector import VectorOperations as vec

def run():
    vertices = [Vertex(Vector(0, 0), 1),
                Vertex(Vector(1, 0), 1),
                Vertex(Vector(1, 1), 1),
                Vertex(Vector(0, 1), 1)]
    
    square = Body(vertices)
    square.draw()

    plt.show()

if __name__ == '__main__':
    run()