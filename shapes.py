import numpy as np


class Circle:
    def __init__(self, radius, k=10**2):
        self.radius = radius
        self.shape = "Circle"
        self.k = k

    def collapse(self, place, e):
        if e.shape == "Circle":
            return abs(self.radius + e.radius - np.linalg.norm(e.place-place, ord=1)) * self.k


class InnerCircle:
    def __init__(self, radius, k=10**4):
        self.radius = radius
        self.shape = "InnerCircle"
        self.k = k

    def collapse(self, place, e):
        if e.shape == "Circle":
            return abs(self.radius - e.radius - np.linalg.norm(e.place-place, ord=1)) * self.k
