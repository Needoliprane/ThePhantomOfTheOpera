import random

from GameClass.Player                           import Player
from GameClass.Room                             import Room
from GameClass.RunningJob                       import RunningJob

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
        self.room = []
        self.players = []
        self.jobTools = None
        self.numberOfRoom = numberOfRoom
        self.numberOfPlayer = numberOfPlayer
        self.inspectorId = 0
        self.phantomId = 0
        self.isRunning = True
        self.singerStatus = 30

#---------------------------------------------- Build game elem
    def buildPlayerList(self):
        oursHeroes = random.sample(range(0, self.numberOfPlayer), 2)
        inspector = self.inspectorId = oursHeroes[0]
        phantom = self.phantomId = oursHeroes[1]

        for id in list(range(self.numberOfPlayer)):
            if (id == inspector) : player = CONFIG[str(id)](self.room[0], True, False, id, self.numberOfRoom, self.room)
            elif (id == phantom) : player = CONFIG[str(id)](self.room[0], False, True, id, self.numberOfRoom, self.room)
            else : player = CONFIG[str(id)](self.room[0], False, False, id, self.numberOfRoom, self.room)
            self.players.append(player)
            self.room[0].addPlayerInTheRoom(player)

    def buildRoomList(self): 
        for i in range(0, self.numberOfRoom):
            self.room.append(Room(i))

    def buildJob(self):
        self.jobTools = RunningJob(self.inspectorId, self.phantomId, self.room, self.numberOfRoom)

    def initGame(self):
        self.buildRoomList()
        self.buildPlayerList()
        self.buildJob()
#---------------------------------------------- Build game element

#---------------------------------------------- Manage win condition
    def updateSingerStatus(self, screamList):
        oldSingerStatus = self.singerStatus
        runningJobList = list(map(lambda room:room.isRunningJob(), self.room))
        if (True not in screamList and True not in runningJobList):
            self.singerStatus += 17
        if (self.singerStatus > 150):
            self.isRunning = False
            print("Victory for the opera")
        if (self.singerStatus < 0):
            print("Phantom Win")
            self.isRunning = False
        if (oldSingerStatus == self.singerStatus):
            self.singerStatus -= 2

    def killPhantom(self, inspectorGuess):
        playerId = next((item for item in inspectorGuess if item is not None), None)
        if (playerId == None):
            return
        if (self.players[playerId].isPhantom == True):
            if (self.players[playerId].UseAlibi() == False):
                self.isRunning = False
                print("You find the phantom !")
            else:
                print("He wasn't the phantom")
        else:
            print("He wasn't the phantom")
#---------------------------------------------- Manage win condition

    def GameLoop(self):
        while self.isRunning == True:
            self.jobTools.addJobs()
            print("job ->", list(map(lambda room:room.isRunningJob(), self.room)))
            list(map(lambda player:player.smartMove(), self.players))
            list(map(lambda player:player.smartMove(True), self.players))
            list(map(lambda player:player.playerDoJob(), self.players))
            print("job ->", list(map(lambda room:room.isRunningJob(), self.room)))

            list(map(lambda player:player.playerDoAction(self.players), self.players))

            scream = list(map(lambda player:player.scream(), self.players))
            print(scream)

            print(list(map(lambda player:player.inspectorWork(scream, self.players), self.players)))

            guess = list(map(lambda player:player.guessPhantom(), self.players))
            self.killPhantom(guess)

            self.updateSingerStatus(scream)
            print("singer status =>",self.singerStatus)

