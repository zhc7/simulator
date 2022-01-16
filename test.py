import numpy as np
from shapes import *
from simulator import World
from Entity import Entity


Box = Entity(InnerCircle(10), 10**5, np.ndarray((0, 0)), 0, 0)
c1 = Entity(Circle(1), 2, np.ndarray((0, 0)), np.ndarray((3, 4)), 0)
c2 = Entity(Circle(1), 2, np.ndarray((3, 5)), np.ndarray((5, -4)), 0)
c3 = Entity(Circle(1), 2, np.ndarray((-3, -4)), np.ndarray((6, 0)), 0)


world = World([Box, c1, c2, c3], {"g": (0, 0)})
