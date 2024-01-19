from abc import ABC, abstractmethod

class IRoofingFactory(ABC):

    @abstractmethod
    def create_material(self):
        pass

    @abstractmethod
    def create_team(self):
        pass