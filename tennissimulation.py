# tennissimulation.py

from tennisplayer import Player
from tennismatch import Match
from random import *

def main():

    pl1 = Player(.5)
    pl2 = Player(.6)
    pl1.setStr("Player 1")
    pl2.setStr("Player 2")
    match = Match(pl1, pl2)

    for i in range(50):
        print(match.runMatch())

main()