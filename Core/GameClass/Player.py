from LogicClass.MonteCarloClass.MonteCarloInspector     import MonteCarloInspector
from LogicClass.MonteCarloClass.MonteCarloMove          import MonteCarloMove
from LogicClass.MonteCarloClass.MonteCarloAction        import MonteCarloAction

class Player:
    def __init__(self, room, isInspector, isPhantom, id, numberOfRoom, roomList):
        self.room = room
        self.isInspector = isInspector
        self.isPhantom = isPhantom
        self.alibi = False
        self.roomList = roomList
        self.id = id
        self.numberOfRoom = numberOfRoom
        self.monteCarloInspector = None
        self.monteCarloMove = None
        self.monteCarloAction = None

#---------------------------------------------- Logical part of player movement
    def playerMove(self, nextRoom):
        if (nextRoom == None or nextRoom.isLock() == True or self.room.isLock() == True):
            print("playerID : ", self.id, " is lock inside roomID ", self.room.id)
            return (False)
        self.room.removePlayerOfTheRoom(self)
        self.room = nextRoom
        self.room.addPlayerInTheRoom(self)
        return (True)

    def smartMove(self, specialTurn=False):
        if (self.monteCarloMove == None): self.monteCarloMove = MonteCarloMove(self.isInspector, self.isPhantom, self.numberOfRoom)
        self.monteCarloMove.wiseMove(self, self.roomList, specialTurn)

    def getRoom(self):
        return self.room
#---------------------------------------------- Logical part of player movement

#---------------------------------------------- Logical part of player alibi
    def getAlibi(self):
        return (self.alibi)

    def UseAlibi(self):
        if (self.alibi == True):
            self.alibi = False
            return (True)
        return (False)
#---------------------------------------------- Logical part of player alibi

#---------------------------------------------- Logical part of player Scream
    def scream(self):
        if (self.isPhantom == True and (len(self.room.getPlayers()) == 1 or self.room.isOn() == False)):
            print("Scream !")
            return (True)
        return (False)
#---------------------------------------------- Logical part of player Scream

#---------------------------------------------- Logical part of player inspector
    def inspectorWork(self, screamList, allPlayers):
        if (self.isInspector == False): return
        if (self.monteCarloInspector == None) : self.monteCarloInspector = MonteCarloInspector()
        self.monteCarloInspector.updateTree(screamList, self.room, allPlayers)
        return self.monteCarloInspector.getPhantom()

    def guessPhantom(self):
        if (self.isInspector == False): return
        if (self.monteCarloInspector == None) : self.monteCarloInspector = MonteCarloInspector()
        return self.monteCarloInspector.guessPhantom()
#---------------------------------------------- Logical part of player inspector

#---------------------------------------------- Logical part of player Job
    def playerDoJob(self):
        if (self.isInspector == False and self.isPhantom == False):
            self.room.doTheJob()
#---------------------------------------------- Logical part of player Job

#---------------------------------------------- Logical part of player Action
    def playerDoAction(self, players):
        if (self.monteCarloAction == None) : self.monteCarloAction = MonteCarloAction(self.isInspector, self.isPhantom, self.numberOfRoom, self.id)
        self.monteCarloAction.manageAction(self.roomList, self, players)
#---------------------------------------------- Logical part of player Action