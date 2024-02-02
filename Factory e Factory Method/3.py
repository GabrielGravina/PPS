from abc import ABC

# Partes da casa
class Foundation(ABC):
    def build(self):
        pass

class Walls(ABC):
    def build(self):
        pass

class Roof(ABC):
    def build(self):
        pass

# Fábrica abstrata
class HouseFactory(ABC):
    def create_foundation(self):
        pass

    def create_walls(self):
        pass

    def create_roof(self):
        pass

# Fábricas concretas
class ContemporaryHouseFactory(HouseFactory):
    def create_foundation(self):
        return ConcreteFoundation()

    def create_walls(self):
        return GlassWalls()

    def create_roof(self):
        return FlatRoof()

class ColonialHouseFactory(HouseFactory):
    def create_foundation(self):
        return StoneFoundation()

    def create_walls(self):
        return BrickWalls()

    def create_roof(self):
        return SlopedRoof()

# Partes concretas da casa
class ConcreteFoundation(Foundation):
    def build(self):
        print("Fundação de concreto construída")

class StoneFoundation(Foundation):
    def build(self):
        print("Fundação de pedra construída")

class GlassWalls(Walls):
    def build(self):
        print("Paredes de vidro construídas")

class BrickWalls(Walls):
    def build(self):
        print("Paredes de tijolo construídas")

class FlatRoof(Roof):
    def build(self):
        print("Telhado plano construído")

class SlopedRoof(Roof):
    def build(self):
        print("Telhado inclinado construído")

# Cliente
class ConstructionSite:
    def __init__(self, house_factory):
        self.foundation = house_factory.create_foundation()
        self.walls = house_factory.create_walls()
        self.roof = house_factory.create_roof()

    def construct(self):
        self.foundation.build()
        self.walls.build()
        self.roof.build()

if __name__ == "__main__":
    contemporary_factory = ContemporaryHouseFactory()
    colonial_factory = ColonialHouseFactory()

    contemporary_construction = ConstructionSite(contemporary_factory)
    colonial_construction = ConstructionSite(colonial_factory)

    print("Construindo casa contemporânea:")
    contemporary_construction.construct()

    print("\nConstruindo casa colonial:")
    colonial_construction.construct()
