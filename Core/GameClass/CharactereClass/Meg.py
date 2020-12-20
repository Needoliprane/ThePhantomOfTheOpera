from GameClass.Player import Player

class Meg(Player):

    def actions(self, room, otherPerson, otherPersons):
        self.playerMove(room)