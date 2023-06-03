import unittest

from src.decorator import Decorator, StrongAnt, SmartAnt, HealthyAnt
from src.prototype import AntPrototype


class DecoratorTestCase(unittest.TestCase):
    def setUp(self):
        base_ant = AntPrototype(10, 5, 100)
        self.decorated_ant = Decorator(base_ant)

    def test_decorator_subclasses_modify_attributes(self):
        base_ant = AntPrototype(10, 5, 100)

        strong_ant = StrongAnt(base_ant)
        self.assertEqual(strong_ant.strength, 20)

        smart_ant = SmartAnt(base_ant)
        self.assertEqual(smart_ant.memory, 10)

        healthy_ant = HealthyAnt(base_ant)
        self.assertEqual(healthy_ant.health, 100)

    def test_multiple_decorators_at_once(self):
        base_ant = AntPrototype(10, 5, 100)
        strong_smart_healthy_ant = HealthyAnt(SmartAnt(StrongAnt(base_ant.clone())))
        strong_strong_smart_ant = StrongAnt(StrongAnt(SmartAnt(base_ant.clone())))
        self.assertEqual(strong_smart_healthy_ant.strength, 20)
        self.assertEqual(strong_smart_healthy_ant.memory, 10)
        self.assertEqual(strong_smart_healthy_ant.health, 100)
        self.assertEqual("Healthy Smart Strong Ant",strong_smart_healthy_ant.name)
        self.assertEqual(strong_strong_smart_ant.strength, 40)
        self.assertEqual(strong_strong_smart_ant.memory, 10)
        self.assertEqual(strong_strong_smart_ant.health, 100)
        self.assertEqual("Strong Strong Smart Ant", strong_strong_smart_ant.name)
