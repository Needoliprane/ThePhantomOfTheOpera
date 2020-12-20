from GameClass.Player import Player

class Persan(Player):

    def actions(self, room, otherPerson, otherPersons):
        self.playerMove(room)
        otherPerson.playerMove(room)