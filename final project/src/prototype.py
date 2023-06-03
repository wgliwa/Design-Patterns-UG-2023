import copy

from src.composite import Component


class AntPrototype(Component):
    def __init__(self, strength, memory, health):
        self.name = "Ant"
        self.strength = strength
        self.memory = memory
        self.health = health

    def clone(self):
        return copy.deepcopy(self)

    def operation(self):
        pass
