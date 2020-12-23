import random

from GameClass.Player                           import Player
from GameClass.Room                             import Room

from GameClass.CharactereClass.Christine        import Christine
from GameClass.CharactereClass.Joseph           import Joseph
from GameClass.CharactereClass.Madame           import Madame
from GameClass.CharactereClass.Meg              import Meg
from GameClass.CharactereClass.Moncharmin       import Moncharmin
from GameClass.CharactereClass.Persan           import Persan
from GameClass.CharactereClass.Raoul            import Raoul
from GameClass.CharactereClass.Richard          import Richard

CONFIG = {
        "0" : Persan,
        "1" : Christine,
        "2" : Joseph,
        "3" : Madame,
        "4" : Meg, 
        "5" : Moncharmin,
        "6" : Raoul,
        "7" : Richard
}

class Game:
    def __init__(self, numberOfRoom, numberOfPlayer):
        self.numberOfRoom = numberOfRoom
        self.room = []
        self.numberOfPlayer = numberOfPlayer
        self.players = []
        self.isRunning = True

    def buildPlayerList(self):
        oursHeroes = random.sample(range(0, self.numberOfPlayer), 2)
        inspector = oursHeroes[0]
        phantom = oursHeroes[1]

        for id in list(range(self.numberOfPlayer)):
            if (id == inspector) : player = CONFIG[str(id)](self.room[0], True, False, id)
            elif (id == phantom) : player = CONFIG[str(id)](self.room[0], False, True, id)
            else : player = CONFIG[str(id)](self.room[0], False, False, id) 
            self.players.append(player)
            self.room[0].addPlayerInTheRoom(player)

    def buildRoomList(self): 
        for i in range(0, self.numberOfRoom):
            self.room.append(Room(i))

    def initGame(self):
        self.buildRoomList()
        self.buildPlayerList()

    def GameLoop(self):
        while (1):
            scream = list(map(lambda player:player.scream(), self.players))
            inspector = list(map(lambda player:player.inspectorWork(scream, self.players), self.players))
