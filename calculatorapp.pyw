# calculatorapp.pyw
from graphics import *
from display import *
from keypad import *
from calculatorengine import *

class CalculatorApp:
    def __init__(self):
        self.win = GraphWin("Calculator", 825, 600)
        self.win.setCoords(0,0,8.25,6)
        self.display = Display(self.win)
        self.keypad = Keypad(self.win)
        self.calcEngine = CalculatorEngine()

    def run(self):
        equation = ''
        #try:
        while True:
            click = self.win.getMouse()
            # Get the key that was pressed
            key = self.keypad.getKey(click)

            try:
                print('key: ' + key)
            except TypeError:
                key = 0
            # Process the key and get the result
            equation = self.calcEngine.parse(equation, key)

            # Display the result
            self.display.update(equation)



def main():
    calc = CalculatorApp()
    calc.run()

main()
