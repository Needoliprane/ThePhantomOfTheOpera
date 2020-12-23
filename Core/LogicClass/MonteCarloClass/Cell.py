import numpy as np

class Cell:
    def __init__(self, head, playerId, parentCell):
        self.head = head
        self.visit = 0
        self.childVisit = 0
        self.value = 0
        self.playerId = playerId
        self.childCell = []
        self.parentCell = parentCell
        self.ucb = 0

    def refreshUCB(self):
        helper = 0
        if (self.childVisit == 0) : helper = 1
        else : helper = self.childVisit
        self.ucb = self.value + 2 * np.sqrt(np.log(self.visit) / helper)
        return (self.ucb)
