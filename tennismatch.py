#tennismatch.py

from tennisplayer import Player
from random import *

class Match:
    def __init__(self, player1, player2):
        self.p1 = player1
        self.p2 = player2
        if random() > .5:
            self.serving = self.p2
            self.other = self.p1
        else:
            self.serving = self.p1
            self.other = self.p2
        self.str = ""


    def runMatch(self):
        m1score = 0
        m2score = 0
        if self.runSet() == self.p1:
            m1score = m1score + 1
        else:
            m2score = m2score + 1

        self.switch()

        if self.runSet() == self.p1:
            m1score = m1score + 1
        else:
            m2score = m2score + 1

        self.switch()

        if m1score == 2:
            return self.p1
        elif m2score == 2:
            return self.p2
        else:
            return self.runSet()

    def runSet(self):
        s1score = 0
        s2score = 0
        i = 0

        while i < 13 and s1score < 6 and s2score < 6:
            if self.runGame() == self.p1:
                s1score = s1score + 1
            else:
                s2score = s2score + 1

            i = i + 1

        if s1score - s2score >= 2:
            self.p1.reset()
            self.p2.reset()
            return self.p1
        elif s2score - s1score >= 2:
            self.p1.reset()
            self.p2.reset()
            return self.p2
        else:
            while abs(s1score-s2score) < 2:
                if runGame() == self.p1:
                    s1score = s1score + 1
                else:
                    s2score = s2score + 1

            if s1score > s2score:
                self.p1.reset()
                self.p2.reset()
                return self.p1
            else:
                self.p1.reset()
                self.p2.reset()
                return self.p2



    def runGame(self):
        while not self.notOver():
            if self.serving.winsSet():
                self.serving.incScore()
            else:
                self.other.incScore()

        if self.serving.getScore() > self.other.getScore():
            return self.serving
        else:
            return self.other



    def notOver(self):
        if self.p1.getScore() < 40 and self.p2.getScore() < 40:
            return False
        elif abs(self.p1.getScore()- self.p2.getScore()) < 2:
            return False
        else:
            return True


    def switch(self):
        if self.serving == self.p1:
            self.serving = self.p2
        else:
            self.serving = self.p1

def main():
    m = Match(Player(.6), Player(.5))
    print(m.runMatch())