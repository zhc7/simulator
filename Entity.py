import numpy as np


class Entity:
    def __init__(self, shape, mass, place, velocity, acceleration):
        self.shape = shape
        self.m = mass
        self.place = place
        self.v = velocity
        self.a = acceleration
        self.forces = []

    def enforce(self, force):
        if force is not None:
            self.forces.append(force)

    def calc_a(self):
        F = 0
        for f in self.forces:
            F += f
        self.a = F / self.m
        self.forces = []

    def collapse(self, e):
        return self.shape.collapse(self.place, e)

    def draw(self, t: Turtle, ratio):
        t.goto(tuple(self.place))
        self.shape.draw(t, ratio)
        return self.place
