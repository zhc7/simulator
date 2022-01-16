import numpy as np


class Entity:
    def __init__(self, mass, place, velocity, acceleration, k):
        self.m = mass
        self.place = place
        self.v = velocity
        self.a = acceleration
        self.k = k
        self.forces = []

    def enforce(self, force):
        self.forces.append(force)

    def calc_a(self):
        F = 0
        for f in self.forces:
            F += f
        self.a = F / self.m

    def collapse(self, e):
        d = self.check_border(e)
        return d * self.k
