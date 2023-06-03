from models.Tank import Tank


class SdKfz165(Tank):
    def __init__(self):
        self.name = "Hummel"
        self.enginge_hp = 162
        self.weight = 24
        self.main_armament_caliber = 150
        self.role = "Self-propelled artillery"
        self.crew = ["driver", "gunner", "loader", "commander", "ammunition_handler", "ammuniation_handler"]
