import time
import pickle
import numpy as np

from Player import Player
from shapes import *
from simulator import World
from Entity import Entity


Box = Entity(InnerCircle(10), 10**5, np.array([0, 0], dtype="float32"), 0, 0)
c1 = Entity(Circle(1), 2, np.array([0, 0], dtype="float32"), np.array([3, 4], dtype="float32"), 0)
c2 = Entity(Circle(1), 2, np.array([3, 5], dtype="float32"), np.array([5, -4], dtype="float32"), 0)
c3 = Entity(Circle(1), 2, np.array([-3, -4], dtype="float32"), np.array([6, 0], dtype="float32"), 0)


world = World([Box, c1, c2, c3], {"g": np.array([0, 0])})

if __name__ == '__main__':
    world.total_time = 1
    t1 = time.time()
    result = world.loop()
    t2 = time.time()
    print(t2 - t1)
    print(len(pickle.dumps(result)), sep="\n")
    p = Player(result[0])
    p.play(result)
