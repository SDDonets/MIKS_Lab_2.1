from IRoofingFactory import IRoofingFactory
from CeramicRoofingMaterial import CeramicRoofingMaterial
from CeramicRoofTeam import CeramicRoofTeam

class CeramicRoofFactory(IRoofingFactory):

    def create_material(self):
        return CeramicRoofingMaterial()

    def create_team(self):
        return CeramicRoofTeam()