from models.american.M1 import M1
from models.american.M18 import M18
from models.american.M26 import M26
from models.american.M3 import M3


class AmericanFactory:
    __instance = None

    def getInstance(self):
        if AmericanFactory.__instance is None:
            AmericanFactory.__instance = AmericanFactory()
        return AmericanFactory.__instance


    def create_tank(self, name):
        return {"M1": M1(),
                "M3": M3(),
                "M18": M18(),
                "M26": M26()}.get(name, None)