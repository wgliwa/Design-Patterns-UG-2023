from src.observator import Subject


class Task(Subject):
    def __init__(self):
        self.task = None
        self.observers = []

    def attach(self, observer):
        self.observers.append(observer)

    def detach(self, observer):
        self.observers.remove(observer)

    def notify(self):
        for i in self.observers:
            i.update(self)

    def add_task(self, task):
        self.task = task
        self.notify()
