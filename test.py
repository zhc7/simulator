import time
import pickle
from Player import Player
from shapes import *
from simulator import World
from Entity import Entity


constants = {"g": np.array([0, -9.8]),
             "epsilon0": 8.854 * 10 ** (-12),
             "pi": 3.14159
             }


Box = Entity(InnerCircle(20), 1, 0, np.array([0, 0], dtype="float32"), 0, 0, fixed=True)
c1 = Entity(Circle(1), 2, 0.0001, np.array([0, 0], dtype="float32"), np.array([3, 4], dtype="float32"), 0)
c2 = Entity(Circle(1), 2, -0.0001, np.array([3, 5], dtype="float32"), np.array([5, -4], dtype="float32"), 0)
c3 = Entity(Circle(1), 2, -0.0001, np.array([-3, -4], dtype="float32"), np.array([6, 0], dtype="float32"), 0)
c4 = Entity(Circle(1), 2, 0, np.array([-10, 10], dtype="float32"), np.array([0, 0], dtype="float32"), 0)


world = World([Box, c1, c2, c3], constants, tic=0.0001)

if __name__ == '__main__':
    world.total_time = 10
    t1 = time.time()
    result = world.loop(0.1)
    t2 = time.time()
    print(t2 - t1)
    print(len(pickle.dumps(result)), sep="\n")
    p = Player(result[0])
    # input()
    p.play(result, record_rate=0.1)
