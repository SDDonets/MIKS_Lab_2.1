from IRoofingFactory import IRoofingFactory
from MetalRoofFactory import MetalRoofFactory
from CeramicRoofFactory import CeramicRoofFactory

import random

factories = [MetalRoofFactory(), CeramicRoofFactory()]

# We choose a random factory
factory = random.choice(factories)

# We create material through the factory
material = factory.create_material()

# We create a team through the factory
team = factory.create_team()

# We display the description of the material and the team
print(material.get_description())
print(team.get_description())