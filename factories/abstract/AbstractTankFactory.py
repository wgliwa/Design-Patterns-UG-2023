from abc import ABC, abstractmethod


class AbstractTankFactory(ABC):
    @abstractmethod
    def create_tank(self, nation, name):
        raise NotImplementedError()