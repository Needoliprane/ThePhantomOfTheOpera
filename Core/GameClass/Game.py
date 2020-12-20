from GameClass.Player import Player
from GameClass.Room import Room

class Game:
    def __init__(self, numberOfRoom, numberOfPlayer):
        self.numberOfRoom = numberOfRoom
        self.room = []
        self.numberOfPlayer = numberOfPlayer
        self.player = []

    def initGame(self):
        for i in range(0, self.numberOfRoom):
            self.room.append(Room(i))
        for i in range(0, self.numberOfPlayer):
            self.player.append(Player(self.room[0], False, False))
            self.room[0].addPlayerInTheRoom(self.player[i])