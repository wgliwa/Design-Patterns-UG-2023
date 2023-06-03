import unittest

from src.builder import Director
from src.decorator import Decorator
from src.prototype import AntPrototype
from src.task import Task

base_ant = AntPrototype(strength=20, memory=20, health=20)


class MainTestCase(unittest.TestCase):
    def test_simple(self):
        ants = []
        for i in range(100):
            ants.append(Decorator.create_random_ant(base_ant))

        task = Task()
        director = Director(ants)
        task.attach(director)
        task.add_task("BringObject")
        task.add_task("OvercomeObstacle")
        task.add_task("BringObject")
        task.add_task("FightEnemy")

    def test_no_ants_left(self):
        ants = []
        for i in range(100):
            ants.append(Decorator.create_random_ant(base_ant))

        task = Task()
        director = Director(ants)
        task.attach(director)
        task.add_task("BringObject")
        task.add_task("OvercomeObstacle")
        task.add_task("FightEnemy")
        task.add_task("BringObject")
        task.add_task("OvercomeObstacle")
        task.add_task("FightEnemy")
        task.add_task("BringObject")
        task.add_task("OvercomeObstacle")
        task.add_task("FightEnemy")

        self.assertNotEqual(0, len(director.tasks))

    def test_swarm_adaptility(self):
        ants = []
        for i in range(100):
            ants.append(Decorator.create_random_ant(base_ant))

        task = Task()
        director = Director(ants)
        task.attach(director)

        task.add_task("BringObject")
        task.add_task("BringObject")
        task.add_task("BringObject")
        task.add_task("BringObject")

        print("###################")
        task2 = Task()
        director2 = Director(ants)
        task2.attach(director2)

        task2.add_task("BringObject")
        task2.add_task("OvercomeObstacle")
        task2.add_task("FightEnemy")
        task2.add_task("BringObject")

    def test_swarm_traits(self):
        ants = [AntPrototype(800, 1, 1), AntPrototype(600, 1, 1), AntPrototype(200, 1, 1), ]

        task = Task()
        director = Director(ants)
        task.attach(director)

        task.add_task("BringObject")
        task.add_task("BringObject")
        self.assertEqual(director.swarms_created[0].traits["strength"], 1000)
        self.assertEqual(director.swarms_created[0].traits["health"], 2)
        self.assertEqual(len(director.swarms_created), 1)
