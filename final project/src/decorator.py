import copy
import random

from src.prototype import AntPrototype


class Decorator(AntPrototype):
    def __init__(self, base_ant):
        super().__init__(base_ant.strength, base_ant.memory, base_ant.health)
        self.base_ant = base_ant

    def clone(self):
        return copy.deepcopy(self)

    @staticmethod
    def create_random_ant(base_ant):
        decorators = [StrongAnt, SmartAnt, HealthyAnt]
        num_decorators = random.randint(1, len(decorators))
        for _ in range(num_decorators):
            decorator_cls = random.choice(decorators)
            base_ant = decorator_cls(base_ant)

        return base_ant


class StrongAnt(Decorator):
    def __init__(self, base_ant):
        super().__init__(base_ant)
        self.name = "Strong " + self.base_ant.name
        self.strength = min(2 * self.strength, 100)


class SmartAnt(Decorator):
    def __init__(self, base_ant):
        super().__init__(base_ant)
        self.name = "Smart " + self.base_ant.name
        self.memory = min(2 * self.memory, 100)


class HealthyAnt(Decorator):
    def __init__(self, base_ant):
        super().__init__(base_ant)
        self.name = "Healthy " + self.base_ant.name
        self.health = min(2 * self.health, 100)
