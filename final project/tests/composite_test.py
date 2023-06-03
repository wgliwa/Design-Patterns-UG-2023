import unittest

from src.composite import Swarm


class SwarmTestCase(unittest.TestCase):
    def test_swarm_operation(self):
        swarm = Swarm("Swarm 1")

        class MockAnt:
            def operation(self):
                self.operation_called = True

        ant1 = MockAnt()
        ant2 = MockAnt()
        swarm.add_child(ant1)
        swarm.add_child(ant2)
        swarm.operation()
        self.assertTrue(ant1.operation_called)
        self.assertTrue(ant2.operation_called)
