from abc import ABC, abstractmethod

class IRoofingTeam(ABC):

    @abstractmethod
    def get_description(self):
        pass