from models.Tank import Tank


class M18(Tank):
    def __init__(self):
        self.name = "Hellcat"
        self.enginge_hp = 400
        self.weight = 17.7
        self.main_armament_caliber = 76
        self.role = "Tank Destroyer"
        self.crew = ["driver", "gunner", "loader", "commander", "radio_operator"]
