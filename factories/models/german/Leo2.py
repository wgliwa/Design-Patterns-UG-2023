from models.Tank import Tank


class Leo2(Tank):
    def __init__(self):
        self.name = "Leopard 2"
        self.enginge_hp = 1500
        self.weight = 68.8
        self.main_armament_caliber = 120
        self.role = "Main Battle Tank"
        self.crew = ["driver", "gunner", "loader", "commander"]