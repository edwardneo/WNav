import random
from vector import Vector

def gen_null():
    def trans_vel():
        while True:
            yield Vector(0, 0)
    
    def ang_vel():
        while True:
            yield 0
    
    return trans_vel(), ang_vel()

def gen_trans():
    def trans_vel():
        while True:
            yield Vector(random.uniform(-1, 1), random.uniform(-1, 1))
    
    def ang_vel():
        while True:
            yield 0
    
    return trans_vel(), ang_vel()

def gen_ang():
    def trans_vel():
        while True:
            yield Vector(0, 0)
    
    def ang_vel():
        while True:
            yield random.uniform(-1, 1)
    
    return trans_vel(), ang_vel()

def gen_trans_ang():
    def trans_vel():
        while True:
            yield Vector(random.uniform(-1, 1), random.uniform(-1, 1))
    
    def ang_vel():
        while True:
            yield random.uniform(-1, 1)
    
    return trans_vel(), ang_vel()

def gen_alt():
    def trans_vel():
        while True:
            trans_vel = Vector(random.uniform(-1, 1), random.uniform(-1, 1))
            yield from [trans_vel, trans_vel]
    
    def ang_vel():
        yield 0
        while True:
            ang_vel = random.uniform(-1, 1)
            yield from [ang_vel, ang_vel]
    
    return trans_vel(), ang_vel()