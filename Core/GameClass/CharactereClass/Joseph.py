from GameClass.Player import Player

class Joseph(Player):

    def actions(self, room, otherPerson, otherPersons):
        if self.room.isOn() == True:
            self.room.switchOffTheLight()
        else:
            self.room.switchOnTheLight()