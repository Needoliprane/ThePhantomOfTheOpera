from GameClass.Player import Player

class Moncharmin(Player):

    def actions(self, room, otherPerson, otherPersons):
        for player in self.room.getPlayers():
            player.playerMove(room)
