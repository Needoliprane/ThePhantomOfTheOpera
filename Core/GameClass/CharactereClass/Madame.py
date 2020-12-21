from GameClass.Player import Player

class Madame(Player):

    def actions(self, room, otherPerson, otherPersons):
        if self.room.isLock() == True:
            self.room.unlockTheRoom()
        else :
            self.room.lockTheRoom()