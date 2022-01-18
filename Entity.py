from __future__ import annotations
from turtle import Turtle
import numpy as np
from shapes import Shape


class Entity:
    def __init__(self, shape: Shape, mass: float,
                 place: np.ndarray, velocity: np.ndarray | int, acceleration: np.ndarray | int, fixed=False):
        self.shape = shape
        self.m = mass
        self.place = place
        self.v = velocity
        self.a = acceleration
        self.forces = []
        self.fixed = fixed

    def enforce(self, force: np.ndarray):
        if self.fixed:
            return
        if force is not None:
            self.forces.append(force)

    def calc_a(self):
        F = 0.0
        for f in self.forces:
            F += f
        self.a = F / self.m
        self.forces = []

    def collapse(self, e: 'Entity'):
        return self.shape.collapse(self.place, e)

    def draw(self, t: Turtle, ratio):
        t.goto(tuple(self.place))
        self.shape.draw(t, ratio)
        return self.place
