from LogicClass.MonteCarloClass.ArborescenteTree import ArborescenteTree

class MonteCarloAction:
    def __init__(self, isInspector, isPhantom, numberOfRoom):
        self.tree = ArborescenteTree()
        self.isPhantom = isPhantom
        self.isInspector = isInspector
        self.numberOfRoom = numberOfRoom

    