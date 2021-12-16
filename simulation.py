import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

from shapes import *
from generators import *

def run():
    obj = WeightedSquare()

    console = False
    
    if not console:
        fig, ax = plt.subplots()
        ln, = plt.plot([], [], '.b-')

        gen_trans_vel, gen_ang_vel = gen_alt()

        def init():
            ax.set_xlim(-2, 2)
            ax.set_ylim(-2, 2)
            return ln,

        def update(frame):
            obj.step()
            x_data, y_data = obj.set_data()
            ln.set_data(x_data, y_data)
            return ln,
        
        def onclick(event):
            obj.trans_vel, obj.ang_vel = next(gen_trans_vel), next(gen_ang_vel)
        
        fig.canvas.mpl_connect('button_press_event', onclick)

        ani = FuncAnimation(fig, update, frames=np.linspace(0, 100),
                            init_func=init, interval=obj.time_step*1000, blit=True)
        plt.show()
    else:
        obj.display()

if __name__ == '__main__':
    run()