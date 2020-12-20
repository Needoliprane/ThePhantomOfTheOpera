from GameClass.Player import Player

class Christine(Player):

    def actions(self, room, otherPerson, otherPersons):
        for player in otherPersons:
            player.playerMove(self.room)