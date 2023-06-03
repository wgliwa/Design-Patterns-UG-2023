from models.Tank import Tank


class M26(Tank):
    def __init__(self):
        self.name = "Pershing"
        self.enginge_hp = 500
        self.weight = 46.0
        self.main_armament_caliber = 90
        self.role = "Heavy Tank"
        self.crew = ["driver", "gunner", "loader", "commander", "radio_operator"]