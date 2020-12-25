from LogicClass.MonteCarloClass.ArborescenteTree import ArborescenteTree

class MonteCarloInspector:
    def __init__(self):
        self.tree = ArborescenteTree()

    def updateTree(self, screamList, room, allPlayers):
        if (True not in screamList): return

        if (room.isOn() == True):
            missingOnes = set(allPlayers).difference(set(room.getPlayers()))
            while missingOnes:
                missingOne = missingOnes.pop()
                self.tree.addPossibilities(id=missingOne.id)
        else:
            for player in room.getPlayers():
                self.tree.addPossibilities(id=player.id)

    def getPhantom(self):
        res = list(map(lambda x:x.refreshUCB(),self.tree.headCell.childCell))
        return (res)

    def guessPhantom(self):
        res = list(map(lambda x:x.refreshUCB(),self.tree.headCell.childCell))
        if (len(res) == 1 and res[0] > 3):
            return (self.tree.headCell.childCell[0].playerId)
        return self.tree.chooseLeaf(self.tree.headCell)