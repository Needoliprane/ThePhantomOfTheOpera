import random

class MonteCarloAction:
    def __init__(self, isInspector, isPhantom, numberOfRoom, id):
        self.isPhantom = isPhantom
        self.isInspector = isInspector
        self.numberOfRoom = numberOfRoom
        self.id = id

    def managePersanAction(self, roomList, player, players):
        if ((self.isPhantom == False and self.isInspector == False) or self.isPhantom == True):
            return
        if (player.monteCarloInspector== None):
            return
        playerId = player.monteCarloInspector.tree.chooseLeaf(player.monteCarloInspector.tree.headCell, maxVal=5)
        if (playerId == None): return
        runningJobList = list(map(lambda room:room.isRunningJob(), roomList))
        if (True in runningJobList):
            res = [i for i, x in enumerate(runningJobList) if x]
            player.actions(roomList[res[0]], players[playerId], None)
            players[playerId].playerDoJob()
            runningJobList = list(map(lambda room:room.isRunningJob(), roomList))
            if (True in runningJobList):
                player.monteCarloInspector.tree.addPossibilities(playerId, 20)

    def manageChristineAction(self, roomList, player, players):
        if ((self.isPhantom == False and self.isInspector == False) or self.isPhantom == True):
            return
        if (player.monteCarloInspector == None):
            return
        playerId = player.monteCarloInspector.tree.chooseLeaf(player.monteCarloInspector.tree.headCell, maxVal=5)
        if (playerId == None): return
        player.actions(None, None, [players[playerId]])

    def manageJosephAction(self, roomList, player, players):
        if (self.isPhantom == True):
            player.actions(None, None, None)

    def manageMadameAction(self, roomList, player, players):
        # No real use find
        pass

    def manageMegAction(self, roomList, player, players):
        # No real use find
        pass

    def manageMoncharminAction(self, roomList, player, players):
        if (self.isPhantom == False):
            return
        newRoomIndex = random.randint(0, self.numberOfRoom - 1)
        if (newRoomIndex == player.room.id):
            self.manageMoncharminAction(roomList, player, players)
        player.actions(roomList[newRoomIndex], None, None)

    def manageRaoulAction(self, roomList, player, players):
        # Too strong unfair
        pass

    def manageRichardAction(self, roomList, player, players):
        # No real use find
        pass

    def manageAction(self, roomList, player, players):
        if (self.id == 0):
            self.managePersanAction(roomList, player, players)
        if (self.id == 1):
            self.manageChristineAction(roomList, player, players)
        if (self.id == 2):
            self.manageJosephAction(roomList, player, players)
        if (self.id == 3):
            self.manageMadameAction(roomList, player, players)
        if (self.id == 4):
            self.manageMegAction(roomList, player, players)
        if (self.id == 5):
            self.manageMoncharminAction(roomList, player, players)
        if (self.id == 6):
            self.manageRaoulAction(roomList, player, players)
        if (self.id == 7):
            self.manageRichardAction(roomList, player, players)