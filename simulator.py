import numpy as np
import pickle

from typing import *

from Entity import Entity


class World:
    def __init__(self, entities: List[Entity], constants: Dict, mode="display", tic=0.01, total_time="infinite"):
        self.entities = entities
        self.constants = constants
        self.mode = mode
        self.tic = tic
        self.total_time = total_time
        self.g = self.constants["g"]

    def step(self) -> None:
        # 运动学循环
        for e in self.entities:
            e.v += self.tic * e.a
            e.place += self.tic * e.v + self.tic ** 2 * e.a / 2

        # 碰撞循环
        for e1 in self.entities:
            for e2 in self.entities:
                if e1 == e2:
                    continue
                F_12 = e1.collapse(e2)
                e2.enforce(F_12)
                e1.enforce(-F_12)
            e1.enforce(self.g)

        # 力学循环
        for e in self.entities:
            e.calc_a()

    def loop(self) -> List[bytes]:
        t = 0
        inf = self.total_time == "infinite"
        record = []
        while inf or t < self.total_time:
            self.step()
            if self.mode == "display":
                record.append(pickle.dumps(self))
            t += self.tic
        return record
