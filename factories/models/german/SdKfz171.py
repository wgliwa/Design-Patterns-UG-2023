from models.Tank import Tank


class SdKfz171(Tank):
    def __init__(self):
        self.name = "Panther"
        self.enginge_hp = 700
        self.weight = 48.8
        self.main_armament_caliber = 75
        self.role = "Medium Tank"
        self.crew = ["driver", "gunner", "loader", "commander","radio operator"]