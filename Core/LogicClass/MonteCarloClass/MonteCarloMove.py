import random

from LogicClass.MonteCarloClass.ArborescenteTree import ArborescenteTree

class MonteCarloMove:
    def __init__(self, isInspector, isPhantom, numberOfRoom):
        self.tree = ArborescenteTree()
        self.isPhantom = isPhantom
        self.isInspector = isInspector
        self.numberOfRoom = numberOfRoom

    def wiseMovePhantom(self, player, roomList):
        roomPossibilities = random.sample(range(0, self.numberOfRoom), self.numberOfRoom - (int(self.numberOfRoom / 2)))
        for roomIndex in roomPossibilities:
            if (roomList[roomIndex].isOn() == False and len(roomList[roomIndex].getPlayers()) > 1):
                self.tree.addPossibilities(roomList[roomIndex].id, value=30)
            elif (roomList[roomIndex].isOn() == False):
                self.tree.addPossibilities(roomList[roomIndex].id, value=15)
            elif (len(roomList[roomIndex].getPlayers()) == 0):
                self.tree.addPossibilities(roomList[roomIndex].id, value=10)
            else:
                self.tree.addPossibilities(roomList[roomIndex].id)
        roomId = self.tree.chooseLeafMove(self.tree.headCell)
        self.tree.headCell.childCell = []
        if (roomId != None):
            player.playerMove(roomList[roomId])
            return
        player.playerMove(roomList[random.randint(0, self.numberOfRoom - 1)])

    def wiseMoveInspector(self, player, roomList):
        if (player.monteCarloInspector == None):
            value = random.randint(0, self.numberOfRoom - 1)
            player.playerMove(roomList[value])
            return
        roomPossibilities = random.sample(range(0, self.numberOfRoom), self.numberOfRoom - (int(self.numberOfRoom / 2)))
        for roomIndex in roomPossibilities:
            for playerInTheRoom in roomList[roomIndex].getPlayers():
                value = player.monteCarloInspector.tree.checkPresenceInTheNodeMove(playerInTheRoom.id, player.monteCarloInspector.tree.headCell.childCell, value=0)
                if (value[0] == True):
                    self.tree.addPossibilities(roomIndex, value[1])
                else:
                    self.tree.addPossibilities(roomIndex, value=1)
        roomId = self.tree.chooseLeafMove(self.tree.headCell)
        self.tree.headCell.childCell = []
        if (roomId != None):
            roomList[roomId].switchOnTheLight()
            player.playerMove(roomList[roomId])
            return
        value = random.randint(0, self.numberOfRoom - 1)
        roomList[value].switchOnTheLight()
        player.playerMove(roomList[value])

    def wiseMoveCharacter(self, player, roomList):
        roomPossibilities = random.sample(range(0, self.numberOfRoom), int(self.numberOfRoom / 2))
        for roomIndex in roomPossibilities:
            if (roomList[roomIndex].isRunningJob() == True):
                self.tree.addPossibilities(roomList[roomIndex].id, value=10)
            else:
                self.tree.addPossibilities(roomList[roomIndex].id)
        roomId = self.tree.chooseLeafMove(self.tree.headCell)
        self.tree.headCell.childCell = []
        if (roomId != None):
            roomList[roomId].switchOnTheLight()
            player.playerMove(roomList[roomId])
            return
        value = random.randint(0, self.numberOfRoom - 1)
        roomList[value].switchOnTheLight()
        player.playerMove(roomList[value])

    def wiseMove(self, player, roomList, specialTurn):
        if (self.isPhantom == True and specialTurn == True):
            self.wiseMovePhantom(player, roomList)
            return
        if (self.isInspector == True and specialTurn == True):
            self.wiseMoveInspector(player, roomList)
            return
        self.wiseMoveCharacter(player, roomList)

