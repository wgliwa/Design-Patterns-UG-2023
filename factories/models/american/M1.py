from models.Tank import Tank


class M1(Tank):
    def __init__(self):
        self.name = "Abrams"
        self.enginge_hp = 1500
        self.weight = 67.6
        self.main_armament_caliber = 120
        self.role = "Main Battle Tank"
        self.crew = ["driver", "gunner", "loader", "commander"]