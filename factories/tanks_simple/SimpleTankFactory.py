from models.american.M1 import M1
from models.american.M18 import M18
from models.american.M26 import M26
from models.american.M3 import M3


class SimpleTankFactory:
    __instance = None

    def getInstance(self):
        if SimpleTankFactory.__instance is None:
            SimpleTankFactory.__instance = SimpleTankFactory()
        return SimpleTankFactory.__instance



    def create_tank(self, name):
        return {"M1": M1(),
                "M3": M3(),
                "M18": M18(),
                "M26": M26()}.get(name, None)
