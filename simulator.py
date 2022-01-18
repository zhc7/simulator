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
            e.place += self.tic * e.v  # + self.tic ** 2 * e.a / 2

        # 碰撞循环
        for i in range(len(self.entities)):
            e1 = self.entities[i]
            for j in range(i+1, len(self.entities)):
                e2 = self.entities[j]
                F = e1.collapse(e2, self.constants)
                e2.enforce(F)
                e1.enforce(-F)
            e1.enforce(self.g)

        # 力学循环
        for e in self.entities:
            e.calc_a()

    def loop(self, record_rate=0.1) -> List[bytes]:
        """record_rate: expected time span between recording"""
        t = 0
        inf = self.total_time == "infinite"
        record = []
        n = 0
        while inf or t < self.total_time:
            self.step()
            if self.mode == "display":
                if t >= record_rate * n:
                    record.append(pickle.dumps(self))
                    n += 1
            t += self.tic
        return record
