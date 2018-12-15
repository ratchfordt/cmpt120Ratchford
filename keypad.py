# keypad.py
from button import *

class Keypad:
    def __init__(self, win):
        self.buttons = [
            Button(win, Point(1,1), .75, .75, '-/+'),
            Button(win, Point(1.75,1), .75, .75, '0'),            
            Button(win, Point(2.5,1), .75, .75, '.'),
            Button(win, Point(3.25,1), .75, .75, '='),
            
            Button(win, Point(1,1.75), .75, .75, '1'),
            Button(win, Point(1.75,1.75), .75, .75, '2'),
            Button(win, Point(2.5, 1.75), .75, .75, '3'),
            Button(win, Point(3.25, 1.75), .75, .75, '-'),
            
            Button(win, Point(1,2.5), .75, .75, '4'),
            Button(win, Point(1.75,2.5), .75, .75, '5'),
            Button(win, Point(2.5,2.5), .75, .75, '6'),
            Button(win, Point(3.25, 2.5), .75, .75, '+'),
            
            Button(win, Point(1,3.25), .75, .75, '7'),
            Button(win, Point(1.75,3.25), .75, .75, '8'),
            Button(win, Point(2.5,3.25), .75, .75, '9'),
            Button(win, Point(3.25, 3.25), .75, .75, '/'),
            Button(win, Point(4, 3.25), .75, .75, '*'),

            #Keypad 2
            Button(win, Point(5,3.25), .75, .75, 'sin'),
            Button(win, Point(5.75,3.25), .75, .75, 'cos'),
            Button(win, Point(6.5,3.25), .75, .75, 'tan'),
            Button(win, Point(7.25, 3.25), .75, .75, '1/x'),

            Button(win, Point(5, 2.5), .75, .75, 'asin'),
            Button(win, Point(5.75, 2.5), .75, .75, 'acos'),
            Button(win, Point(6.5, 2.5), .75, .75, 'atan'),
            Button(win, Point(7.25, 2.5), .75, .75, 'log'),

            Button(win, Point(5, 1.75), .75, .75, 'C'),
            Button(win, Point(5.75, 1.75), .75, .75, '('),
            Button(win, Point(6.5, 1.75), .75, .75, ')'),

            Button(win, Point(.2,5.8), .4, .4, 'q')
            ]

    def getKey(self, p):
        for button in self.buttons:
            if button.clicked(p):
                return button.getLabel()
