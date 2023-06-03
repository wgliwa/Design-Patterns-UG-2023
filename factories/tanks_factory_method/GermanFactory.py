from models.german.Jagd38t import Jagd38t
from models.german.Leo2 import Leo2
from models.german.SdKfz165 import SdKfz165
from models.german.SdKfz171 import SdKfz171


class GermanFactory:
    __instance = None

    def getInstance(self):
        if GermanFactory.__instance is None:
            GermanFactory.__instance = GermanFactory()
        return GermanFactory.__instance


    def create_tank(self, name):
        return {"Jagd38t": Jagd38t(),
                "Leo2": Leo2(),
                "SdKfz165": SdKfz165(),
                "SdKfz171": SdKfz171()}.get(name, None)
