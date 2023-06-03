import unittest

from tanks_factory_method.TankFactory import TankFactory


class Test(unittest.TestCase):
    def test_create_german_tank(self):
        factory = TankFactory().getInstance()
        tank = factory.create_tank("Leo2", "germany")
        self.assertEqual(tank.name, "Leopard 2")

    def test_create_american_tank(self):
        factory = TankFactory().getInstance()
        tank = factory.create_tank("M1", "usa")
        self.assertEqual(tank.name, "Abrams")

    def test_create_tank_invalid(self):
        factory = TankFactory().getInstance()
        with self.assertRaises(Exception):
            tank = factory.create_tank("dfggdfg", "usaadfsf")