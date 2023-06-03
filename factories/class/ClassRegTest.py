import pstats
import random
import cProfile
from ClassReg import ClassReg
from abstract.TankFactoryA import TankFactoryA
from models.Tank import Tank
from models.american.M1 import M1
from models.american.M18 import M18
from models.american.M26 import M26
from models.american.M3 import M3
from tanks_factory_method.TankFactory import TankFactory
from tanks_simple.SimpleTankFactory import SimpleTankFactory

reg = ClassReg().getInstance()
simple_car_factory = SimpleTankFactory().getInstance()
method_car_factory = TankFactory()
abstract_car_factory = TankFactoryA()
tank_types = ['M1', 'M3', "M18", "M26"]


def create_tanks_simple():
    for i in range(100000):
        car_type = random.choice(tank_types)
        simple_car_factory.create_tank(car_type)


def create_tanks_method():
    for i in range(100000):
        car_type = random.choice(tank_types)
        method_car_factory.create_tank(car_type, "usa")


def create_tanks_abstract():
    for i in range(100000):
        car_type = random.choice(tank_types)
        abstract_car_factory.create_tank(car_type, "usa")


def register_tanks_with_reflection():
    for i in range(100000):
        car_type = random.choice(tank_types)
        reg.register_tank(car_type, Tank)
        reg.create_tank(car_type)


def register_tanks_without_reflection():
    for i in range(100000):
        car_type = random.choice(tank_types)
        if car_type == 'M1':
            reg.register_tank('M1', M1)
        elif car_type == 'M8':
            reg.register_tank('M3', M3)
        elif car_type == 'M18':
            reg.register_tank('M18', M18)
        elif car_type == 'M26':
            reg.register_tank('M26', M26)
        reg.create_tank(car_type)


cProfile.run('create_tanks_simple()', 'prof')
print("Simple")
pstats.Stats('prof').print_stats('time')
cProfile.run('create_tanks_method()', 'prof')
print("Method")
pstats.Stats('prof').print_stats('time')
cProfile.run('create_tanks_abstract()', 'prof')
print("Abstract")
pstats.Stats('prof').print_stats('time')
cProfile.run('register_tanks_with_reflection()', 'prof')
print("Reflection")
pstats.Stats('prof').print_stats('time')
cProfile.run('register_tanks_without_reflection()', 'prof')
print("Without Reflection")
pstats.Stats('prof').print_stats('time')
