class Strategy:
    def do_operation(self, ants):
        pass


class BringObject(Strategy):
    name = "BringObject"

    def do_operation(self, ants):
        strength_threshold = 1000
        sorted_ants = sorted(ants, key=lambda x: x.strength - x.memory - x.health, reverse=True)
        selected_ants = []
        total_strength = 0

        for ant in sorted_ants:
            if total_strength == strength_threshold:
                break
            if total_strength < strength_threshold:
                selected_ants.append(ant)
                total_strength += ant.strength
            elif (total_strength - selected_ants[-1].strength) + ant.strength - \
                    strength_threshold < total_strength - strength_threshold:
                total_strength += ant.strength - selected_ants[-1].strength
                selected_ants[-1] = ant

        if total_strength >= strength_threshold:
            return selected_ants
        else:
            return None


class OvercomeObstacle(Strategy):
    name = "OvercomeObstacle"

    def do_operation(self, ants):
        strength_threshold = 500
        memory_threshold = 800
        sorted_ants = sorted(ants, key=lambda x: x.memory + x.strength - x.health, reverse=True)
        selected_ants = []
        total_strength = 0
        total_memory = 0

        for ant in sorted_ants:
            if total_strength == strength_threshold and total_memory == memory_threshold:
                break
            if total_strength < strength_threshold or total_memory < memory_threshold:
                selected_ants.append(ant)
                total_strength += ant.strength
                total_memory += ant.memory
            elif ((total_strength - selected_ants[
                -1].strength) + ant.strength - strength_threshold < total_strength - strength_threshold) \
                    and ((total_memory - selected_ants[
                -1].memory) + ant.memory - memory_threshold < total_memory - memory_threshold):
                total_strength += ant.strength - selected_ants[-1].strength
                total_memory += ant.memory - selected_ants[-1].memory
                selected_ants[-1] = ant

        if total_strength >= strength_threshold and total_memory >= memory_threshold:
            return selected_ants
        else:
            return None


class FightEnemy(Strategy):
    name = "FightEnemy"

    def do_operation(self, ants):
        health_threshold = 800
        memory_threshold = 200
        sorted_ants = sorted(ants, key=lambda x: x.health + x.memory - x.strength, reverse=True)
        selected_ants = []
        total_health = 0
        total_memory = 0

        for ant in sorted_ants:
            if total_health == health_threshold and total_memory == memory_threshold:
                break
            if total_health < health_threshold or total_memory < memory_threshold:
                selected_ants.append(ant)
                total_health += ant.health
                total_memory += ant.memory
            elif ((total_health - selected_ants[
                -1].health) + ant.health - health_threshold < total_health - health_threshold) \
                    and ((total_memory - selected_ants[
                -1].memory) + ant.memory - memory_threshold < total_memory - memory_threshold):
                total_health += ant.health - selected_ants[-1].health
                total_memory += ant.memory - selected_ants[-1].memory
                selected_ants[-1] = ant

        if total_health >= health_threshold:
            return selected_ants
        else:
            return None
