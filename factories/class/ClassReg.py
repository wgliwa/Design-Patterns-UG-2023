from models.american.M1 import M1
from models.american.M18 import M18
from models.american.M26 import M26
from models.american.M3 import M3


class ClassReg:
    _tank_classes = {}
    __instance = None

    def getInstance(self):
        if ClassReg.__instance is None:
            ClassReg()
        return ClassReg.__instance

    def __init__(self):
        if ClassReg.__instance is None:
            ClassReg.__instance = self

    def create_tank(self, name):
        return {"M1": M1(),
                "M3": M3(),
                "M18": M18(),
                "M26": M26()}.get(name, None)

    def register_tank(cls, tank_type,tank_class):
        cls._tank_classes[tank_type] = tank_class
