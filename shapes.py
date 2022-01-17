from __future__ import annotations

import numpy
import numpy as np
import math
from turtle import Turtle

from Entity import Entity


class Circle:
    def __init__(self, radius: int, k=10**2, color="blue"):
        self.radius = radius
        self.shape = "Circle"
        self.k = k
        self.color = color

    def collapse(self, place: numpy.ndarray, e: Entity) -> np.ndarray | int:
        if isinstance(e.shape, Circle):
            d = e.place - place
            m = np.linalg.norm(d)
            f = max(self.radius + e.shape.radius - m, 0) * self.k
            return np.array(f * d / m)
        return 0

    def draw(self, t: Turtle, ratio):
        t.fillcolor(self.color)
        t.begin_fill()
        t.goto((np.array(t.pos()) - np.array([0, self.radius]))*ratio)
        t.circle(self.radius*ratio)
        t.end_fill()


class InnerCircle:
    def __init__(self, radius: int, k=10**4):
        self.radius = radius
        self.shape = "InnerCircle"
        self.k = k

    def collapse(self, place, e: Entity) -> np.ndarray | int:
        if isinstance(e.shape, Circle):
            d = e.place - place
            m = np.linalg.norm(d)
            f = min(self.radius - e.shape.radius - m, 0) * self.k
            return np.array(f * d / m)
        return 0

    def draw(self, t: Turtle, ratio):
        t.begin_fill()
        t.goto((np.array(t.pos()) - np.array([0, self.radius]))*ratio)
        t.circle(self.radius*ratio)
        t.end_fill()
