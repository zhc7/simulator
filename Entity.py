import numpy as np


class Entity:
    def __init__(self, mass, place, velocity, acceleration):
        self.m = mass
        self.place = place
        self.v = velocity
        self.a = acceleration
        self.forces = []

    def enforce(self, force):
        self.forces.append(force)

    def calc_a(self):
        F = 0
        for f in self.forces:
            F += f
        self.a = F / self.m
