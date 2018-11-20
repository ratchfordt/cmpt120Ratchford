#tennisplayer.py

from random import *

class Player:

    def __init__(self, prob):
        self.p = prob
        self.score = 0
        self.set = 0
        self.str = ""

    def setStr(self, string):
        self.str = string

    def __str__(self):
        return self.str

    def getP(self):
        return self.p

    def incScore(self):
        if self.score == 0:
            self.score = 15
        elif self.score == 15:
            self.score = 30
        elif self.score == 30:
            self.score = 40
        else:
            self.score = self.score + 1

    def incSet(self):
        self.set = self.set + 1

    def getScore(self):
        return self.score

    def getSet(self):
        return self.set

    def winsSet(self):
        if random() > self.p:
            return True
        return False

    def reset(self):
        self.score = 0