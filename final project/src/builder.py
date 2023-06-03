from src.composite import Swarm
from src.observator import Observer
from src.strategy import BringObject, OvercomeObstacle, FightEnemy


class Builder():
    def __init__(self):
        self.strategy = None
        self.swarm = None
        self.ants_needed = None

    def add_swarm(self, swarm):
        self.swarm = swarm

    def set_strategy(self, strategy):
        self.strategy = strategy

    def get_ants_needed(self):
        return self.ants_needed

    def check_strategy_viabilty(self, free_ants):
        self.ants_needed = self.strategy.do_operation(free_ants)
        if self.ants_needed:
            return True

    def add_ants_to_swarm(self):
        self.swarm.extend_children(self.ants_needed)

    def add_traits_to_swarm(self):
        for ant in self.swarm.children:
            self.swarm.traits["strength"] += ant.strength
            self.swarm.traits["memory"] += ant.memory
            self.swarm.traits["health"] += ant.health

    def reset(self):
        self.strategy = None
        self.swarm = None
        self.ants_needed = None


class Director(Observer):
    def __init__(self, ants):
        self.builder = Builder()
        self.free_ants = ants
        self.tasks = []
        self.swarms_created = []

    def update(self, subject):
        self.tasks.append(subject.task)
        self.construct_swarm(self.select_strategy(subject.task), subject.task)

    def select_strategy(self, task):
        strategy_mapping = {
            "BringObject": BringObject,
            "OvercomeObstacle": OvercomeObstacle,
            "FightEnemy": FightEnemy
        }

        if task in strategy_mapping:
            return strategy_mapping[task]()

    def construct_swarm(self, strategy, task):
        self.builder.add_swarm(Swarm("Swarm " + str(len(self.swarms_created))))
        self.builder.set_strategy(strategy)
        if self.builder.check_strategy_viabilty(self.free_ants):
            self.tasks.remove(task)
            tmp = self.builder.get_ants_needed()
            self.free_ants = [ant for ant in self.free_ants if ant not in tmp]
            self.builder.add_ants_to_swarm()
            self.builder.add_traits_to_swarm()
            swarm_created = self.builder.swarm
            self.swarms_created.append(swarm_created)
            print(
                f"Created {swarm_created.name} with {len(swarm_created.children)} ants,"
                f" {len(self.free_ants)} ants left, strategy used {self.builder.strategy.name} ")

            self.builder.reset()
        else:
            swarm_created = None
            print("Uh oh stinky")

        return swarm_created
