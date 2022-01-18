from __future__ import annotations
import numpy as np
from turtle import Turtle
import typing
if typing.TYPE_CHECKING:
    from Entity import Entity


class Shape:
    def collapse(self, place: np.ndarray, e: Entity, r: float) -> np.ndarray | int:
        pass

    def draw(self, t: Turtle, ratio: float):
        pass


class Circle(Shape):
    def __init__(self, radius: int, k=10**2, color="blue"):
        self.radius = radius
        self.shape = "Circle"
        self.k = k
        self.color = color

    def collapse(self, place: np.ndarray, e: Entity, r: float) -> np.ndarray | int:
        if isinstance(e.shape, Circle):
            if r > (self.radius + e.shape.radius):
                return 0
            d = e.place - place
            f = (self.radius + e.shape.radius - r) * (self.k + e.shape.k)
            return np.array(f * d / r)
        return 0

    def draw(self, t: Turtle, ratio):
        t.fillcolor(self.color)
        t.begin_fill()
        t.goto((np.array(t.pos()) - np.array([0, self.radius]))*ratio)
        t.circle(self.radius*ratio)
        t.end_fill()


class InnerCircle(Shape):
    def __init__(self, radius: int, k=10**4):
        self.radius = radius
        self.shape = "InnerCircle"
        self.k = k

    def collapse(self, place, e: Entity, r: float) -> np.ndarray | int:
        if isinstance(e.shape, Circle):
            if r < (self.radius - e.shape.radius):
                return 0
            d = e.place - place
            f = (self.radius - e.shape.radius - r) * self.k
            return np.array(f * d / r)
        return 0

    def draw(self, t: Turtle, ratio):
        t.begin_fill()
        t.goto((np.array(t.pos()) - np.array([0, self.radius]))*ratio)
        t.circle(self.radius*ratio)
        t.end_fill()
