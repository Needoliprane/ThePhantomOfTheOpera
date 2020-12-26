#!/usr/local/bin/python

import time
from statistics import mean

import matplotlib.pyplot as plt

from GameClass.Game                     import Game

NUMBER_OF_RUN = 1000

def masterbBenchmark():
    res = []
    durationList = []

    for i in range(0, NUMBER_OF_RUN):
        start = time.time()
        gameController = Game(12, 8)
        gameController.initGame()
        value = gameController.GameLoop()
        print("Phantom wins ? ", value)
        stop = time.time()
        res.append(value)
        durationList.append(stop-start)

    nbWin = res.count(True)
    print("Phantom wins :", nbWin, "or,", (nbWin * 100) / NUMBER_OF_RUN, "%")
    print("Run time moyen :", mean(durationList))
    print("Run time min :", min(durationList))
    print("Run time max :", max(durationList))
    plt.plot(durationList)
    plt.ylabel('time')
    plt.show()

if __name__ == "__main__":
    masterbBenchmark()