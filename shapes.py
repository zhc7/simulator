import numpy as np


class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.shape = "Circle"

    def collapse(self, e):
        if e.shape == "Circle":
            return abs(self.radius + e.radius - np.linalg.norm(e.place-self.place, ord=1))
