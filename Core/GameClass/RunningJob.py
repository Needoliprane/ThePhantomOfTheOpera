import random

class RunningJob:
    def __init__(self, inspectorId, phantomId, roomList, numberOfRoom):
        self.inspectorId = inspectorId
        self.phantomId = phantomId
        self.roomList = roomList
        self.numberOfRoom = numberOfRoom

    def addJobs(self):
        print(self.numberOfRoom)
        jobList = random.sample(range(0, self.numberOfRoom), int(self.numberOfRoom / 2))
        print(jobList)
        for index in jobList:
            self.roomList[index].addTheJob()
