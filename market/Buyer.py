import random

from Observer import Observer, Subject
from Visitor import Visitor, Component


class Buyer(Subject, Observer, Component):
    _observers: list[Observer] = []

    def __init__(self, luxury_want, minimum_default_buy, money=3500):
        self.money = money
        self.previous_money = money
        self.mood = random.uniform(-1.0, 1.0)
        self.bought_value = 0
        self.wanted_products = []
        self.luxury_want = luxury_want
        self.minimum_default_buy = minimum_default_buy
        self.inflation = 1.0

    def generate_wanted_luxuries(self, names):
        for i in names:
            if (not i.luxury and random.random() > 0.5) or (i.luxury and random.random() > 0.8):
                self.wanted_products.append(i)

    def attach(self, observer: Observer):
        self._observers.append(observer)

    def detach(self, observer: Observer):
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update(self)

    def update(self, subject: Subject):
        from Seller import Seller
        from Bank import Bank
        if isinstance(subject, Seller):
            self.buy(subject)
        if isinstance(subject, Bank):
            self.inflation = subject.inflation

    def next(self):
        x = random.uniform(self.previous_money, self.previous_money + 1000)
        self.money = x + x * self.inflation
        # print(self.money)
        self.previous_money = self.money
        self.minimum_default_buy = self.money * random.random()
        self.luxury_want = random.random()

    def accept(self, visitor: Visitor):
        visitor.visit_buyer(self)

    def buy(self, seller):
        # print(self.money, self.inflation, )
        for i in seller.merchandise:
            if ((i.luxury and random.random() > self.luxury_want) or (
                    not i.luxury and self.minimum_default_buy > 0)) and i.calculate_price(
                self.inflation) <= self.money and i.quantity > 0:
                self.money -= i.calculate_price(self.inflation)
                self.bought_value = i.calculate_price(self.inflation)
                self.minimum_default_buy -= i.calculate_price(self.inflation)
                i.quantity -= 1
                self.notify()
                self.bought_value = 0
