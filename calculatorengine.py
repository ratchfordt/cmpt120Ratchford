# calculatorengine.py

import math

class CalculatorEngine:
    def __init__(self):
        pass

    def process(self, key):
        if key == "+/-":
            return "-"
        else:
            return key

    def solve(self, eq):
        try:
            eq = eq.split()
        except AttributeError:
            if type(eq) is int:
                return eq
            else:
                eq = list(eq)


        #try:
        while '(' in eq or ')' in eq or '*' in eq or '/' in eq or '+' in eq or '-' in eq:
            if '(' in eq:
                i1 = eq.index('(')
                i2 = eq.index(')')
                eq[i2] = self.solve(eq[(i1+1):i2])
                del eq[i1:i2]

            elif '*' in eq:
                i = eq.index('*')
                if eq[i+1] == '-':
                    eq[i+2] = 0 - int(eq[i+2])
                    del eq[i+1]
                eq[i+1] = int(eq[i-1])*int(eq[i+1])
                del eq[(i-1):(i+1)]

            elif '/' in eq:
                i = eq.index('/')
                if eq[i+1] == '-':
                    eq[i+2] = 0 - int(eq[i+2])
                    del eq[i+1]
                eq[i+1] = int(eq[i-1])/int(eq[i+1])
                del eq[(i-1):(i+1)]

            elif '+' in eq:
                i = eq.index('+')
                if eq[i+1] == '-':
                    eq[i+2] = 0 - int(eq[i+2])
                    del eq[i+1]
                eq[i+1] = int(eq[i-1])+int(eq[i+1])
                del eq[(i-1):(i+1)]

            elif '-' in eq:
                i = eq.index('-')
                if eq[i+1] == '-':
                    eq[i+2] = 0 - int(eq[i+2])
                    del eq[i+1]
                eq[i+1] = int(eq[i-1])-int(eq[i+1])
                del eq[(i-1):(i+1)]

        return int(eq[0])
        #except:
        #    return 0

    def parse(self, eq, new):
        try:
            int(new)
            eq = str(eq) + new
        except ValueError:
            if new == '+/-':
                if eq[0] == '-':
                    del eq[0]
                else:
                    eq = '-' + eq
            elif new == '=':
                eq = self.solve(eq)

            elif new == 'sin':
                eq = math.sin(self.solve(eq))

            elif new == 'cos':
                eq = math.cos(self.solve(eq))

            elif new == 'tan':
                eq = math.tan(self.solve(eq))

            elif new == 'asin':
                eq = math.asin(self.solve(eq))

            elif new == 'acos':
                eq = math.acos(self.solve(eq))

            elif new == 'atan':
                eq = math.atan(self.solve(eq))

            elif new == '1/x':
                eq = 1/(self.solve(eq))

            elif new == 'log':
                eq = log(self.solve(eq))

            elif new == 'C':
                eq = ''

            elif new == 'q':
                exit()

            else:
                if eq == '':
                    return ''
                else:
                    eq = str(eq) + ' ' + new + ' '

        return eq
            
