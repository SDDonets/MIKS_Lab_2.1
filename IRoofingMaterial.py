from abc import ABC, abstractmethod

class IRoofingMaterial(ABC):

    @abstractmethod
    def get_description(self):
        pass