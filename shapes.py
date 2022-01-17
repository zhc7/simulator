import numpy as np
import math


class Circle:
    def __init__(self, radius, k=10**2):
        self.radius = radius
        self.shape = "Circle"
        self.k = k

    def collapse(self, place, e):
        if e.shape == "Circle":
            d = e.place - place
            m = math.sqrt(np.linalg.norm(d))
            f = max(self.radius + e.radius - m, 0) * self.k
            return np.array(f * d / m)
        return 0


class InnerCircle:
    def __init__(self, radius, k=10**4):
        self.radius = radius
        self.shape = "InnerCircle"
        self.k = k

    def collapse(self, place, e):
        if e.shape == "Circle":
            d = e.place - place
            m = math.sqrt(np.linalg.norm(d))
            f = min(self.radius - e.radius - m, 0) * self.k
            return np.array(f * d / m)
        return 0
