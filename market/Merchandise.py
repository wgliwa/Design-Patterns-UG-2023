import random


class Merchandise:
    def __init__(self, name, cost, luxury):
        self.name = name
        self.cost = cost
        self.quantity = random.randint(0, 10)
        self.profit = random.uniform(1.1, 1.5)
        self.luxury = luxury

    def calculate_price(self, inflation):
        return (self.cost + self.cost * inflation) * self.profit

    def new_shipment(self):
        self.quantity = random.randint(0, 30)

    def change_profit(self):
        if self.quantity == 0:
            self.profit += 0.1
        elif self.profit > 0:
            self.profit = max(self.profit - 0.1, 0.1)

    def change_manufactoring_cost(self, inflation):
        self.cost += self.cost * inflation
