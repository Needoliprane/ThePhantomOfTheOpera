class Room:
    def __init__(self, id):
        self.light = True
        self.lock = False
        self.roomId = id
        self.playerInTheRoom = []


    def getPlayers(self):
        return (self.playerInTheRoom)

#---------------------------------------------- Logical part of Room and player
    def removePlayerOfTheRoom(self, p):
        if (self.lock == True):
            return (False)
        self.playerInTheRoom.remove(p)
        return (True)

    def addPlayerInTheRoom(self, p):
        if (self.lock == True):
            return (False)
        self.playerInTheRoom.append(p)
        return (True)
#---------------------------------------------- Logical part of Room and player

#---------------------------------------------- Logical part of Room and Light
    def switchOffTheLight(self):
        self.light = False

    def switchOnTheLight(self):
        self.light = True

    def isOn(self):
        return (self.light)
#---------------------------------------------- Logical part of Room and Light

#---------------------------------------------- Logical part of Room and Lock
    def unlockTheRoom(self):
        self.lock = False

    def lockTheRoom(self):
        self.lock = True

    def isLock(self):
        return self.lock
#---------------------------------------------- Logical part of Room and Lock