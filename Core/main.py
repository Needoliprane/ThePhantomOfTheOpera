#!/usr/local/bin/python

from GameClass.Game                     import Game

def master():
    gameController = Game(12, 8)
    gameController.initGame()
    value = gameController.GameLoop()
    print("Phantom wins ? ", value)

if __name__ == "__main__":
    master()