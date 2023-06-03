from models.Tank import Tank


class Jagd38t(Tank):
    def __init__(self):
        self.name = "Hetzer"
        self.enginge_hp = 160
        self.weight = 17.75
        self.main_armament_caliber = 75
        self.role = "Tank Destroyer"
        self.crew = ["driver", "gunner", "loader", "commander"]