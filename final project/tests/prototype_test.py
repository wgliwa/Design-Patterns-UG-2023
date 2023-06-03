import unittest

from src.prototype import AntPrototype


class AntPrototypeTestCase(unittest.TestCase):
    def setUp(self):
        self.ant_prototype = AntPrototype(10, 5, 100)

    def test_clone_returns_copy_with_same_attributes(self):
        ant_clone = self.ant_prototype.clone()
        self.assertIsInstance(ant_clone, AntPrototype)
        self.assertIsNot(ant_clone, self.ant_prototype)
        self.assertEqual(ant_clone.name, self.ant_prototype.name)
        self.assertEqual(ant_clone.strength, self.ant_prototype.strength)
        self.assertEqual(ant_clone.memory, self.ant_prototype.memory)
        self.assertEqual(ant_clone.health, self.ant_prototype.health)

    def test_clone_creates_independent_copy(self):
        ant_clone = self.ant_prototype.clone()
        ant_clone.name = "Cloned Ant"
        ant_clone.strength = 15
        ant_clone.memory = 8
        ant_clone.health = 120

        self.assertNotEqual(ant_clone.name, self.ant_prototype.name)
        self.assertNotEqual(ant_clone.strength, self.ant_prototype.strength)
        self.assertNotEqual(ant_clone.memory, self.ant_prototype.memory)
        self.assertNotEqual(ant_clone.health, self.ant_prototype.health)


if __name__ == '__main__':
    unittest.main()
