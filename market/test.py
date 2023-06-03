import random
import unittest

import matplotlib.pyplot as plt

from Bank import Bank
from Buyer import Buyer
from Merchandise import Merchandise
from Seller import Seller
from Visitor import ConcreteVisitor

apple = Merchandise("apple", 80, False)
bread = Merchandise("bread", 20, False)
water = Merchandise("water", 30, False)
car = Merchandise("car", 2000, True)
phone = Merchandise("phone", 3000, True)
merchandise = [apple, bread, car, phone, water]
visitor = ConcreteVisitor()


class TestNoInteference(unittest.TestCase):
    def test_no_inteference(self):
        buyers, sellers, money, inflation = [], [], [], []
        bank = Bank()
        inflation = []
        for i in range(10):
            sellers.append(Seller(merchandise, 0.0))
        for i in range(50):
            buyers.append(Buyer(random.random(), random.random()))

        for i in sellers:
            bank.attach(i)
            for j in buyers:
                i.attach(j)

        for j in buyers:
            j.attach(bank)
            bank.attach(j)

        for i in range(100):
            for b in buyers:
                b.accept(visitor)
            for s in sellers:
                s.accept(visitor)
            bank.accept(visitor)
            inflation.append(bank.inflation)
            money.append(bank.money_value)

        # plt.plot(inflation, label="inflation")
        # plt.title("Inflation")
        # plt.show()

        fig, axs = plt.subplots(2)
        fig.suptitle('Inflation and money value')
        axs[0].plot(inflation)
        axs[1].plot(money)
        plt.show()


class TestWithInteference(unittest.TestCase):
    def test_with_inteference(self):
        buyers, sellers, money, inflation = [], [], [], []
        bank = Bank()
        inflation = []
        for i in range(10):
            sellers.append(Seller(merchandise, 0.0))
        for i in range(50):
            buyers.append(Buyer(random.random(), random.random()))

        for i in sellers:
            bank.attach(i)
            for j in buyers:
                i.attach(j)

        for j in buyers:
            j.attach(bank)
            bank.attach(j)

        for i in range(200):
            if i == 40:
                # for s in buyers:
                #     x = s.previous_money
                #     s.previous_money *= 2000
                #     print(x, s.previous_money)
                for s in sellers:
                    for m in s.merchandise:
                        m.profit *= 2000

            for b in buyers:
                b.accept(visitor)
            for s in sellers:
                s.accept(visitor)
            bank.accept(visitor)
            inflation.append(bank.inflation)
            money.append(bank.money_value)

        # plt.plot(inflation, label="inflation")
        # plt.title("Inflation")
        # plt.show()

        fig, axs = plt.subplots(2)
        fig.suptitle('Inflation and money value')
        axs[0].plot(inflation)
        axs[1].plot(money)
        plt.show()


class TestManufacutringCostJump(unittest.TestCase):
    def test(self):
        buyers, sellers, money, inflation = [], [], [], []
        bank = Bank()
        inflation = []
        for i in range(10):
            sellers.append(Seller(merchandise, 0.0))
        for i in range(50):
            buyers.append(Buyer(random.random(), random.random()))

        for i in sellers:
            bank.attach(i)
            for j in buyers:
                i.attach(j)

        for j in buyers:
            j.attach(bank)
            bank.attach(j)

        for i in range(100):
            if i == 50:
                bank.current_revenue += 600000000
            for b in buyers:
                b.accept(visitor)
            for s in sellers:
                s.accept(visitor)
            bank.accept(visitor)
            inflation.append(bank.inflation)
            money.append(bank.money_value)

        # plt.plot(inflation, label="inflation")
        # plt.title("Inflation")
        # plt.show()

        fig, axs = plt.subplots(2)
        fig.suptitle('Inflation and money value')
        axs[0].plot(inflation)
        axs[1].plot(money)
        plt.show()
