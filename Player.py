from __future__ import annotations
import time
from typing import List
import pickle
from simulator import World
import turtle


class Player:
    def __init__(self, world: World | bytes, ratio=20):
        if type(world) == bytes:
            world = pickle.loads(world)
        self.turtles = [turtle.Turtle() for _ in range(len(world.entities))]
        for t in self.turtles:
            t.penup()
            t.hideturtle()
        self.places = [None] * len(world.entities)
        self.tic = world.tic
        self.ratio = ratio
        self.t_time = turtle.Turtle()
        self.t_time.hideturtle()
        self.t_time.penup()
        self.t_time.goto(-400, 200)

    def draw(self, world: World):
        turtle.tracer(False)
        for i, (e, t) in enumerate(zip(world.entities, self.turtles)):
            if tuple(e.place) != self.places[i]:
                t.clear()
            self.places[i] = tuple(e.draw(t, self.ratio))
        turtle.tracer(True)

    def play(self, worlds: List[World | bytes], fps=10, record_rate=0.1):
        delay = 1 / fps
        n = 0
        slices = []
        for i in range(len(worlds)):
            if i * record_rate >= n * delay:
                slices.append(i)
                n += 1
        t = 0
        t1 = time.time()
        for i in slices:
            world = worlds[i]
            self.draw(world if type(world) == World else pickle.loads(world))
            self.t_time.write(str(round(t, 2)))
            t2 = time.time()
            time.sleep(max(t - (t2 - t1), 0))
            self.t_time.clear()
            t += delay
