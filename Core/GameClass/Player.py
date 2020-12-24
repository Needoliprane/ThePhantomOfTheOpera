from LogicClass.MonteCarloClass.MonteCarloInspector import MonteCarloInspector

class Player:
    def __init__(self, room, isInspector, isPhantom, id):
        self.room = room
        self.isInspector = isInspector
        self.isPhantom = isPhantom
        self.alibi = False
        self.id = id
        self.monteCarloInspector = None

#---------------------------------------------- Logical part of player movement
    def playerMove(self, nextRoom):
        if (nextRoom == None or nextRoom.isLock() == True):
            return (False)
        self.room.removePlayerOfTheRoom(self)
        self.room = nextRoom
        self.room.addPlayerInTheRoom(self)
        return (True)

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
        self.monteCarloInspector.updateTree(screamList, self.room.getPlayers(), allPlayers)
        return self.monteCarloInspector.getPhantom()

    def guessPhantom(self):
        if (self.isInspector == False): return
        if (self.monteCarloInspector == None) : self.monteCarloInspector = MonteCarloInspector()
        return self.monteCarloInspector.guessPhantom()
#---------------------------------------------- Logical part of player inspector