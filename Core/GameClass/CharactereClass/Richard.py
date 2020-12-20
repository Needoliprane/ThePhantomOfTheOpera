from GameClass.Player import Player

class Richard(Player):

    def actions(self, room, otherPerson, otherPersons):
        newRoom = otherPerson.getRoom()
        otherPlayerRoom = self.getRoom()
        self.playerMove(newRoom)
        otherPerson.playerMove(otherPlayerRoom)