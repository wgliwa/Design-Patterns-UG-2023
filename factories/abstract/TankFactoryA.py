from abstract.AbstractTankFactory import AbstractTankFactory
from abstract.AmericanFactoryA import AmericanFactoryA
from abstract.GermanFactoryA import GermanFactoryA
from tanks_factory_method.AmericanFactory import AmericanFactory
from tanks_factory_method.GermanFactory import GermanFactory


class TankFactoryA(AbstractTankFactory):
    def getInstance(self):
        if TankFactoryA.__instance is None:
            TankFactoryA.__instance = TankFactoryA()
        return TankFactoryA.__instance

    def create_tank(self, name,nation):
        f = None
        if nation == "germany":
            f = GermanFactoryA().getInstance()
        elif nation == "usa":
            f = AmericanFactoryA().getInstance()
        if f is None:
            raise Exception("No factory")
        return f.create_tank(name)
