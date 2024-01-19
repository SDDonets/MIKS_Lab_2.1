from IRoofingFactory import IRoofingFactory
from MetalRoofingMaterial import MetalRoofingMaterial
from MetalRoofTeam import MetalRoofTeam

class MetaRoofFactory(IRoofingFactory):
    def create_material(self):
        return MetalRoofingMaterial()

    def create_team(self):
        return MetalRoofTeam()