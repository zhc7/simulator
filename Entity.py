from __future__ import annotations
from turtle import Turtle
from typing import Dict
import numpy as np

from shapes import Shape


class Entity:
    def __init__(self, shape: Shape, mass: float, charge: float,
                 place: np.ndarray, velocity: np.ndarray | int, acceleration: np.ndarray | int, fixed=False):
        self.shape = shape
        self.m = mass
        self.q = charge
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
        if self.fixed:
            return
        F = 0.0
        for f in self.forces:
            F += f
        self.a = F / self.m
        self.forces = []

    def collapse(self, e: 'Entity', constants: Dict):
        r_vector = e.place - self.place
        r = np.linalg.norm(r_vector)
        mechanical = self.shape.collapse(self.place, e, r)
        if self.q:
            electrical = self.q * e.q / (constants["epsilon0"] * 4 * constants["pi"] * r ** 2) * r_vector / r
        else:
            electrical = 0
        return mechanical + electrical

    def draw(self, t: Turtle, ratio):
        t.goto(tuple(self.place))
        self.shape.draw(t, ratio)
        return self.place
