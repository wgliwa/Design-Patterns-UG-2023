import unittest

from src.prototype import AntPrototype
from src.strategy import BringObject


class StrategyTestCase(unittest.TestCase):
    def test_overflow(self):
        ants = [AntPrototype(800, 1, 1), AntPrototype(600, 1, 1), AntPrototype(200, 1, 1), ]
        strategy = BringObject()
        result = strategy.do_operation(ants)
        tmp = 0
        for i in result:
            tmp += i.strength

        self.assertEqual(tmp, 1000)

    def test_overflow2(self):
        ants = [AntPrototype(800, 1, 1), AntPrototype(600, 1, 1), AntPrototype(300, 1, 1), ]
        strategy = BringObject()
        result = strategy.do_operation(ants)
        tmp = 0
        for i in result:
            tmp += i.strength

        self.assertEqual(tmp, 1100)

    def test_sorting(self):
        ants = [AntPrototype(800, 1, 1), AntPrototype(600, 1, 600), AntPrototype(600, 1, 1), ]
        strategy = BringObject()
        result = strategy.do_operation(ants)
        self.assertEqual(result[1].health, 1)
