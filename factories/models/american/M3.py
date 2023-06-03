from models.Tank import Tank


class M3(Tank):
    def __init__(self):
        self.name = "Stuart"
        self.enginge_hp = 250
        self.weight = 14.7
        self.main_armament_caliber = 37
        self.role = "Scout Tank"
        self.crew = ["driver", "gunner", "loader", "commander"]