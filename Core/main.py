#!/usr/local/bin/python

from GameClass.Game import Game
from GameClass.CharactereClass.Meg import Meg
from GameClass.Room import Room

def master():
    gameController = Game(12, 8)
    gameController.initGame()
    gameController.GameLoop()

if __name__ == "__main__":
    master()