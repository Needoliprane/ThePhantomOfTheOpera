class Player:
    def __init__(self, room, isInspector, isPhantom):
        self.room = room
        self.isInspector = isInspector
        self.isPhantom = isPhantom
        self.alibi = False
        self.room.addPlayerInTheRoom(self)

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