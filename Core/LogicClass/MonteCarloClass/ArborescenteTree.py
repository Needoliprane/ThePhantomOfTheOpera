from LogicClass.MonteCarloClass.Cell import Cell

class ArborescenteTree:
    def __init__(self):
        self.headCell = Cell(True, -1, None)

#---------------------------------------------- Logical part of arborescenteTree
    def checkPresenceInTheNode(self, playerId, node):
        for cell in node:
            if playerId == cell.playerId:
                cell.value += 1
                cell.visit += 1
                cell.refreshUCB()
                return (True)
        return False

    def addCoupable(self, playerId):
        if (self.checkPresenceInTheNode(playerId, self.headCell.childCell) == True):
            return
        self.headCell.childCell.append(Cell(False, playerId, self.headCell))
        for cell in self.headCell.childCell:
            if (cell.playerId == playerId) :
                cell.value += 1
                cell.visit += 1
            cell.refreshUCB()

    def chooseLeaf(self, node):
        if (node == None or node.childCell == []):
            return
        res = []
        for cell in node.childCell:
            res.append(cell.refreshUCB())
            cell.visit += 1
            cell.parentCell.childVisit += 1
        self.chooseLeaf(node.childCell[res.index(max(res))])
#---------------------------------------------- Logical part of arborescenteTree