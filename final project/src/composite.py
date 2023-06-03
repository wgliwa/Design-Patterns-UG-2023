from abc import ABC, abstractmethod


class Component(ABC):
    @abstractmethod
    def operation(self):
        pass


class Swarm(Component):
    def __init__(self, name):
        self.name = name
        self.children = []
        self.traits = {"strength": 0, "memory": 0, "health": 0}

    def add_child(self, child):
        self.children.append(child)

    def remove_child(self, child):
        self.children.remove(child)

    def extend_children(self, children):
        self.children.extend(children)

    def operation(self):
        print(f"Composite {self.name} operation")
        for child in self.children:
            child.operation()
