from GameClass.Player import Player

class Madame(Player):

    def actions(self, room, otherPerson, otherPersons):
        if self.room.isLock() == True:
            self.room.lockTheRoom()
        if self.room.isLock() == False:
            self.room.unlockTheRoom()