from Buyer import Buyer
from Observer import Observer, Subject
from Visitor import Visitor, Component


class Bank(Subject, Observer, Component):

    def __init__(self):
        self.observers = []
        self.current_revenue = 0.0
        self.previous_revenue = 0.0
        self.inflation = 0.0
        self.money_value = 0

    def attach(self, observer: Observer):
        self.observers.append(observer)

    def detach(self, observer: Observer):
        self.observers.remove(observer)

    def notify(self):
        for observer in self.observers:
            observer.update(self)

    def update(self, subject: Subject):
        if isinstance(subject, Buyer):
            self.current_revenue += subject.bought_value

    def accept(self, visitor: Visitor):
        visitor.visit_bank(self)

    def next(self):
        if self.previous_revenue == 0:
            self.previous_revenue = self.current_revenue

        if self.current_revenue == 0:
            print("Bankrupt")
            self.previous_revenue = self.current_revenue


        # elif self.previous_revenue > self.current_revenue:
        #     self.inflation -= 0.001
        # elif self.current_revenue > self.previous_revenue:
        #     self.inflation += 0.001

        else:
            self.inflation = (self.current_revenue - self.previous_revenue) / self.previous_revenue

        self.money_value += self.inflation
        self.previous_revenue = self.current_revenue
        self.current_revenue = 0
        self.notify()
