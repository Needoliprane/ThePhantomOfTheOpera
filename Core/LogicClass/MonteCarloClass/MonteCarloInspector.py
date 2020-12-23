from LogicClass.MonteCarloClass.ArborescenteTree import ArborescenteTree

class MonteCarloInspector:
    def __init__(self):
        self.tree = ArborescenteTree()

    def updateTree(self, screamList, playerInTheRoom, allPlayers):
        if (True not in screamList): return

        for player in allPlayers:
            for playerI in playerInTheRoom:
                if (player.id == playerI.id):
                    continue
                else:
                    self.tree.addCoupable(playerId=player.id)

    def getPhantom(self):
        res = list(map(lambda x:x.refreshUCB(),self.tree.headCell.childCell))
        print("UCB => ", res)
        return (res)
