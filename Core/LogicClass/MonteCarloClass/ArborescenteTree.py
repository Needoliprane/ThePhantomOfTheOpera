from LogicClass.MonteCarloClass.Cell import Cell

class ArborescenteTree:
    def __init__(self):
        self.headCell = Cell(True, -1, None)

#---------------------------------------------- Logical part of arborescenteTree
    def checkPresenceInTheNode(self, playerId, node, value=1):
        for cell in node:
            if playerId == cell.playerId:
                cell.value += value
                cell.visit += 1
                cell.refreshUCB()
                return (True)
        return False

    def checkPresenceInTheNodeMove(self, playerId, node, value=1):
        for cell in node:
            if playerId == cell.playerId:
                cell.value += value
                cell.visit += 1
                cell.refreshUCB()
                return (True, cell.value)
        return (False, 0)

    def addPossibilities(self, id, value=1):
        if (self.checkPresenceInTheNode(id, self.headCell.childCell) == True):
            return
        self.headCell.childCell.append(Cell(False, id, self.headCell))
        for cell in self.headCell.childCell:
            if (cell.playerId == id) :
                cell.value += value
                cell.visit += 1
            cell.refreshUCB()

    def chooseLeaf(self, node):
        if (node == None or node.childCell == []):
            return
        res = []
        for cell in node.childCell:
            cell.visit += 1
            cell.parentCell.childVisit += 1
            res.append(cell.refreshUCB())
        if (res.count(max(res)) > 1):
            return
        if (node.childCell[res.index(max(res))].childCell == []):
            return (node.childCell[res.index(max(res))].playerId)
        return self.chooseLeaf(node.childCell[res.index(max(res))])

    def chooseLeafMove(self, node):
        if (node == None or node.childCell == []):
            return
        res = []
        for cell in node.childCell:
            cell.visit += 1
            cell.parentCell.childVisit += 1
            res.append(cell.refreshUCB())
        if (node.childCell[res.index(max(res))].childCell == []):
            return (node.childCell[res.index(max(res))].playerId)
        return self.chooseLeaf(node.childCell[res.index(max(res))])
#---------------------------------------------- Logical part of arborescenteTree