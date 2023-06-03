from tanks_factory_method.AmericanFactory import AmericanFactory
from tanks_factory_method.GermanFactory import GermanFactory


class TankFactory:
    __instance = None

    def getInstance(self):
        if TankFactory.__instance is None:
            TankFactory.__instance = TankFactory()
        return TankFactory.__instance

    def create_tank(self,  name,nation):
        f = None
        if nation == "germany":
            f = GermanFactory().getInstance()
        elif nation == "usa":
            f = AmericanFactory().getInstance()
        if f is None:
            raise Exception("No factory")
        return f.create_tank(name)
