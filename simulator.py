import numpy as np
import time


class World:
    def __init__(self, entities, constants, mode="display", tic=0.01, total_time="infinite"):
        self.entities = entities
        self.constants = constants
        self.mode = mode
        self.tic = tic
        self.total_time = total_time
        self.g = self.constants["g"]

    def step(self):
        # 运动学循环
        for e in self.entities:
            e.v += self.tic * e.a
            e.s += self.tic * e.v + self.tic ** 2 * e.a / 2

        # 碰撞循环
        for e1 in self.entities:
            for e2 in self.entities:
                F_12 = e1.collapse(e2)
                e2.enforce(F_12)
            e1.enforce(self.g)

        # 力学循环
        for e in self.entities:
            e.calc_a()

    def loop(self):
        t = 0
        timestamp = time.time()
        inf = self.total_time is "infinite"
        while inf or t < self.total_time:
            self.step()
            if self.mode == "display":
                time.sleep(self.tic - (time.time() - timestamp))
                # todo: display
            t += self.tic
            timestamp = time.time()
