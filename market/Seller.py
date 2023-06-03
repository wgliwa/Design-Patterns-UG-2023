from Bank import Bank
from Merchandise import Merchandise
from Observer import Observer, Subject
from Visitor import Visitor, Component


class Seller(Subject, Observer, Component):
    def __init__(self, merchandise, inflation):
        self.merchandise = []
        self.merchandise = [Merchandise(item.name, item.cost, item.luxury) for item in merchandise]
        self.inflation = inflation
        self.observers = []

    def attach(self, observer: Observer):
        self.observers.append(observer)

    def detach(self, observer: Observer):
        self.observers.remove(observer)

    def notify(self):
        for observer in self.observers:
            observer.update(self)

    def update(self, subject: Subject):
        self.inflation = subject.inflation

    def accept(self, visitor: Visitor):
        visitor.visit_seller(self)

    def sell_to_subscribers(self):
        for observer in self.observers:
            if (not isinstance(observer, Bank)):
                observer.buy(self)

    def next(self):
        for i in self.merchandise:
            i.change_profit()
            # i.change_manufactoring_cost(self.inflation)
            i.new_shipment()
        self.notify()
